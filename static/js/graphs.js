
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

  var minDate = dateDim.bottom(1)[0]["date"];
  var maxDate = dateDim.top(1)[0]["date"];

  //charts
  var timeChart = dc.barChart("#time-chart");
  // var usChart = dc.geoChoroplethChart("#us-chart");


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



  dc.renderAll();

};
