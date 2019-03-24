
console.log('test');
var payments = crossfilter([
  {date: "2011-11-14T16:17:54Z", quantity: 2, total: 190, tip: 100, type: "tab", productIDs:["001"]},
  {date: "2011-11-14T16:20:19Z", quantity: 2, total: 190, tip: 100, type: "tab", productIDs:["001", "005"]},
  {date: "2011-11-14T16:28:54Z", quantity: 1, total: 300, tip: 200, type: "visa", productIDs:["004" ,"005"]},
  {date: "2011-11-14T16:30:43Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["001", "002"]},
  {date: "2011-11-14T16:48:46Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["005"]},
  {date: "2011-11-14T16:53:41Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["001", "004" ,"005"]},
  {date: "2011-11-14T16:54:06Z", quantity: 1, total: 100, tip: 0, type: "cash", productIDs:["001", "002", "003", "004" ,"005"]},
  {date: "2011-11-14T16:58:03Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["001"]},
  {date: "2011-11-14T17:07:21Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["004" ,"005"]},
  {date: "2011-11-14T17:22:59Z", quantity: 2, total: 90, tip: 0, type: "tab", productIDs:["001", "002", "004" ,"005"]},
  {date: "2011-11-14T17:25:45Z", quantity: 2, total: 200, tip: 0, type: "cash", productIDs:["002"]},
  {date: "2011-11-14T17:29:52Z", quantity: 1, total: 200, tip: 100, type: "visa", productIDs:["004"]}
]);

var paymentsByTotal = payments.dimension(function(d) { return d.total; });

var paymentsByProductID = payments.dimension(function(d) { return d.productIDs; }, true);
var ans = paymentsByProductID.top(Infinity);
console.log(ans);


queue()     //asynchronous call back, when all data loaded , continue to call make graphs
    .defer(d3.json, "/first1/projects")
    .defer(d3.json, "static/geojson/us-states.json")
    .await(makeGraphs);

function makeGraphs(error, projectsJson, statesJson) {    //pass db.proejcts and us-states to function
  console.log('???')
  console.log('???')
  var crimeProjects = projectsJson;
  var dateFormat = d3.time.format("%Y-%m-%d");
  crimeProjects.forEach(function(d){
    d["date"] = dateFormat.parse(d["date"]);
    d["date"].setDate(1);

  });


  var ndx = crossfilter(crimeProjects);

  //Define Dimensions
  var dateDim = ndx.dimension(function(d) { return d["date"]; });
  var stateDim = ndx.dimension(function(d) { return d["state"]; });


  //Calculate metrics
  var numProjectsByDate = dateDim.group();

  var all = ndx.groupAll();

  //Define values (to be used in charts)
	var minDate = dateDim.bottom(1)[0]["date"];
	var maxDate = dateDim.top(1)[0]["date"];

  //charts
  var timeChart = dc.barChart("#time-chart");
  var usChart = dc.geoChoroplethChart("#us-chart");


  timeChart
  .width(600)
  .height(160)
  .margins({top: 10, right: 50, bottom: 30, left: 50})
  .dimension(dateDim)
  .group(numProjectsByDate)
  .transitionDuration(500)
  .x(d3.time.scale().domain([minDate, maxDate]))
  .elasticY(true)
  .xAxisLabel("Year")
  .yAxis().ticks(4);


  usChart.width(1000)
		.height(330)
		.dimension(stateDim)
		.group(numProjectsByDate)
		// .colors(["#E2F2FF", "#C4E4FF", "#9ED2FF", "#81C5FF", "#6BBAFF", "#51AEFF", "#36A2FF", "#1E96FF", "#0089FF", "#0061B5"])
		// .colorDomain([0, max_state])
		.overlayGeoJson(statesJson["features"], "state", function (d) {
			return d.properties.name;
		})
		.projection(d3.geo.albersUsa()
    				.scale(600)
    				.translate([340, 150]))
		// .title(function (p) {
		// 	return "State: " + p["key"]
		// 			+ "\n"
		// 			+ "Total Donations: " + Math.round(p["value"]) + " $";
		// })



  dc.renderAll();

};
