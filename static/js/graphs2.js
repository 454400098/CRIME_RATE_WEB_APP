queue()     //asynchronous call back, when all data loaded , continue to call make graphs
	.defer(d3.json, "/second1/projects2")
    .defer(d3.json, "static/geojson/us-states.json")
    .await(makeGraphs);

function makeGraphs(error,zipJson,statesJson) {    //pass db.proejcts and us-states to function
  var userinput=d3.select("#zip");
  
  console.log(userinput);
  var zipjson=zipJson;
  
  //var userzip2={{userinput['Area']|tojson}};
  console.log(userinput[0]);
  // var dateFormat = d3.time.format("%Y-%m-%d");
  var dateFormat = d3.time.format("%-m/%-d/%Y");
  zipjson.forEach(function(d){
	  
	  
    //d["date"] = dateFormat.parse(d["date"]);
    //d["date"].setDate(1);
    //d["n_killed"]=+d["n_killed"];
    //d["n_injured"]=+d["n_injured"];
    //d["n_teen"]=+d["n_teen"];
	//d["n_male"]=+d["n_male"];
	//d["n_female"]=+d["n_female"];
  });


  //var ndx = crossfilter(crimeProjects);
  /*
  var ndx= crossfilter(zipjson);
var ZipDim = ndx.dimension(function(d) { return d["GEOID"]; });
var a2 =  ndx.dimension(function(d){return d["Total Population"];});
var a3 =  ndx.dimension(function(d){return d["Total Male Population"];});
var a4 =  ndx.dimension(function(d){return d["Total Female Population	White - Total Population"];});
var a5 =  ndx.dimension(function(d){return d["White - Total Male Population"];});
var a6 =  ndx.dimension(function(d){return d["White - Total Female Population"];});
var a7 =  ndx.dimension(function(d){return d["African American - Total Population"];});
var a8 =  ndx.dimension(function(d){return d["African American - Total Male Population"];});
var a9 =  ndx.dimension(function(d){return d["African American - Total Female Population"];});
var a10 =  ndx.dimension(function(d){return d["American Indian - Total Population"];});
var a11 =  ndx.dimension(function(d){return d["American Indian - Total Male Population"];});
var a12 =  ndx.dimension(function(d){return d["American Indian - Total Female Population"];});
var a13 =  ndx.dimension(function(d){return d["Asian - Total Population"];});
var a14 =  ndx.dimension(function(d){return d["Asian - Total Male Population"];});
var a15 =  ndx.dimension(function(d){return d["Asian - Total Female Population"];});
var a16 =  ndx.dimension(function(d){return d["Native Hawaiian - Total Population"];});
var a17 =  ndx.dimension(function(d){return d["Native Hawaiian - Total Male Population"];});
var a18 =  ndx.dimension(function(d){return d["Native Hawaiian - Total Female Population"];});
var a19 =  ndx.dimension(function(d){return d["Other Races - Total Population"];});
var a20 =  ndx.dimension(function(d){return d["Other Races - Total Male Population"];});
var a21 =  ndx.dimension(function(d){return d["Other Races - Total Female Population"];});
var a22 =  ndx.dimension(function(d){return d["Two or More Races - Total Population"];});
var a23 =  ndx.dimension(function(d){return d["Two or More Races - Total Male Population"];});
var a24 =  ndx.dimension(function(d){return d["Two or More Races - Total Female Population"];});
var a25 =  ndx.dimension(function(d){return d["Hispanic or Latino - Total Population"];});
var a26 =  ndx.dimension(function(d){return d["Hispanic or Latino - Total Male Population"];});
var a27 =  ndx.dimension(function(d){return d["Hispanic or Latino - Total Female Population"];});
var a28 =  ndx.dimension(function(d){return d["Median Age"];});
var a29 =  ndx.dimension(function(d){return d["Male - Median Age"];});
var a30 =  ndx.dimension(function(d){return d["Female - Median Age"];});
var a31 =  ndx.dimension(function(d){return d["U.S. citizen, born in the United States"];});
var a32 =  ndx.dimension(function(d){return d["U.S. citizen, born in Puerto Rico or U.S. Island Areas"];});
var a33 =  ndx.dimension(function(d){return d["U.S. citizen, born abroad of American parent(s)"];});
var a34 =  ndx.dimension(function(d){return d["U.S. citizen by naturalization"];});
var a35 =  ndx.dimension(function(d){return d["Not a U.S. citizen"];});
var a36 =  ndx.dimension(function(d){return d["Not a citizen - European"];});
var a37 =  ndx.dimension(function(d){return d["Not a citizen - Asian"];});
var a38 =  ndx.dimension(function(d){return d["Not a citizen - African"];});
var a39 =  ndx.dimension(function(d){return d["Not a citizen - Oceania"];});
var a40 =  ndx.dimension(function(d){return d["Not a citizen - Latin America"];});
var a41 =  ndx.dimension(function(d){return d["Not a citizen - North America"];});
var a42 =  ndx.dimension(function(d){return d["No Income"];});
var a43 =  ndx.dimension(function(d){return d["Total Housing Units"];});
var a44 =  ndx.dimension(function(d){return d["Housing Units - Owner occupied"];});
var a45 =  ndx.dimension(function(d){return d["Housing Units - Renter occupied"];});
var a46 =  ndx.dimension(function(d){return d["Median House Value"];});
var a47 =  ndx.dimension(function(d){return d["Lower Quartile House Value"];});
var a48 =  ndx.dimension(function(d){return d["Upper Quartile House Value"];});
var a49 =  ndx.dimension(function(d){return d["Median Household Income"];});
var a50 =  ndx.dimension(function(d){return d["Average Household Income"];});
var a51 =  ndx.dimension(function(d){return d["Total num of families"];});
var a52 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY Under .50"];});
var a53 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 0.50-0.74"];});
var a54 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 0.75-0.99"];});
var a55 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 1.0-1.24"];});
var a56 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 1.24 - 1.49"];});
var a57 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 1.50 - 1.74"];});
var a58 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 1.75 - 1.84"];});
var a59 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 1.85 - 1.99"];});
var a60 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 2.0 - 2.99"];});
var a61 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 3.0 - 3.99"];});
var a62 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 4.0 - 4.99"];});
var a63 =  ndx.dimension(function(d){return d["RATIO OF INCOME TO POVERTY 5.0 and over"];});
*/
var w = 400;
var h = 400;
var r = h/2;
var aColor = [
    'rgb(178, 55, 56)',
    'rgb(213, 69, 70)',
    'rgb(230, 125, 126)',
    'rgb(239, 183, 182)'
]

var data = [
    {"label":"Colorectale levermetastase (n=336)", "value":74}, 
    {"label": "Primaire maligne levertumor (n=56)", "value":12},
    {"label":"Levensmetatase van andere origine (n=32)", "value":7}, 
    {"label":"Beningne levertumor (n=34)", "value":7}
];


var vis = d3.select('#chart').append("svg:svg").data([data]).attr("width", w).attr("height", h).append("svg:g").attr("transform", "translate(" + r + "," + r + ")");

var pie = d3.layout.pie().value(function(d){return d.value;});

// Declare an arc generator function
var arc = d3.svg.arc().outerRadius(r);

// Select paths, use arc generator to draw
var arcs = vis.selectAll("g.slice").data(pie).enter().append("svg:g").attr("class", "slice");
arcs.append("svg:path")
    .attr("fill", function(d, i){return aColor[i];})
    .attr("d", function (d) {return arc(d);})
;

// Add the text
arcs.append("svg:text")
    .attr("transform", function(d){
        d.innerRadius = 100;
        d.outerRadius = r;
        return "translate(" + arc.centroid(d) + ")";}
    )
    .attr("text-anchor", "middle")
    .text( function(d, i) {return data[i].value + '%';})
;



  dc.renderAll();

};
