queue()     //asynchronous call back, when all data loaded , continue to call make graphs
    .defer(d3.json, "/second/data.json")  //main dataset group by zipcode
    .defer(d3.json, "/first2/projects2")
    .await(makeGraphs);

function makeGraphs(error, projectsJson, zipJson) {


};
