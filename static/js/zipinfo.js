queue()     //asynchronous call back, when all data loaded , continue to call make graphs
    .defer(d3.json, "/second/data.json")  //main dataset group by zipcode
    .await(makeGraphs);

function makeGraphs(error, projectsJson, zipJson) {

};
