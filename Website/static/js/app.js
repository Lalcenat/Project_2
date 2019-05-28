
var default_url = "/line_data_route1"

d3.json(default_url).then(function(data)) {

    var data = [trace1];
    var layout = {title: "GDP and Life Expectancy Over Time"};
    Plotly.plot("line_graph",data,layout);


}

function GetData(route) {
    console.log(route);
    d3.json(`${route}`).then(function(data) {
        console.log('newdata',data);
        updatePlotly(data);

    }):
}

function updatePlotly(newdata) {
    Plotly.restyle("line","x",[newdata.x]);
    Plotly.restyle("line","y",[newdata.y]);

}