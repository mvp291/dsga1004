var padding = 40,
    width = 500,
    height = 500;

var data = [];
var dataset = [];
var xVar, yVar;
var xValue, xScale, xMap, xAxis;
var yValue, yScale, yMap, yAxis;

$(document).ready(
function() {
	d3.csv("car.csv", processData);
});

function processData (error, dataset) {
	var options = [];
	var cols = d3.keys(dataset[0]);
	for (var i = 0; i < cols.length; i++) {
		// Ignore categorical dimentions origin and name
		if (cols[i] == 'origin' || cols[i] == 'name') {
			continue;
		}
		var elem  = {
			'id' : cols[i],
			'name': cols[i]
		};
		options.push(elem);
	}
	dataset.forEach(function (row, ix) {
		for (var i = 0; i < options.length; i++) {
			row[options[i].id] = + row[options[i].id];
		}
	});
	var svg = d3.select('svg')
		.attr("width", width)
		.attr("height", height);
	data = dataset;
	assignSelections(options);
	drawData(options[0].id, options[0].id);
}

function assignSelections (options) {
	var xSelect  = $('#sel-x');
	var ySelect  = $('#sel-y');
	for (var i = 0; i < options.length; i++) {
		var xOpt = options[i];
		$('<option></option>')
			.val(xOpt.id)
			.text(xOpt.name)
			.appendTo(xSelect);
		var yOpt = options[i];
		$('<option></option>')
			.val(yOpt.id)
			.text(yOpt.name)
			.appendTo(ySelect);
	}
}

function subset(xVar, yVar) {
        dataset = [];
        data.forEach(function(row, i) {
                dataset.push([row[xVar], row[yVar], row["name"]]);
        });
        return dataset;
}

function subset_min_max(xVar, yVar, min, max) {
	console.log(min, max);
	dataset = [];
	data.forEach(function(row, i) {
		if (row.mpg >= min && row.mpg <= max) {
			console.log('pushing');
			dataset.push([row[xVar], row[yVar], row["name"]]);
		}
	});
	return dataset;
}

function drawData(xVar, yVar) {
	xVar = xVar;
	yVar = yVar;
	dataset = subset(xVar, yVar);
	xValue = function(d) { return d[0];};
	xScale = d3.scale.linear().range([padding, width - padding*2]);
	xMap = function (d) { return xScale(xValue(d))};
	xAxis = d3.svg.axis().scale(xScale).orient("bottom").ticks(5);
	yValue = function(d) { return d[1];};
	yScale = d3.scale.linear().range([height - padding, padding]);
	yMap = function (d) { return yScale(yValue(d))};
	yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(5);
	xScale.domain([d3.min(dataset, xValue)-2, d3.max(dataset, xValue)+2]);
  	yScale.domain([d3.min(dataset, yValue)-2, d3.max(dataset, yValue)+2]);
  	var svg = d3.select('svg');
  	var selection = svg.selectAll("circle").data(dataset);
  	selection.enter().append("circle")
	    .attr("class", "dot")
	    .attr("r", 3.5)
	    .attr("cx", xMap)
	    .attr("cy", yMap);
	selection.on("mouseover", function(d) {
       	$("#hovered").text(d[2]);
    });

	selection.exit().remove();

	// Add to X axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + (width - padding) +")")
        .call(xAxis);

    // Add to Y axis
    svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + padding +",0)")
        .call(yAxis);

    d3.select('#sel-x')
    	.on('change', function() {
    		xVar = $('#sel-x option:selected').val();
    		dataset = subset(xVar, yVar);
    		console.log(xVar, yVar, dataset[0], dataset[0]);
    		xValue = function(d) { return d[0];};
			xScale = d3.scale.linear().range([padding, width - padding*2]);
			xMap = function (d) { return xScale(xValue(d))};
			xAxis = d3.svg.axis().scale(xScale).orient("bottom").ticks(5);
			xScale.domain([d3.min(dataset, xValue)-2, d3.max(dataset, xValue)+2]);
			var svg = d3.select('svg');
		  	var selection = svg.selectAll("circle").data(dataset, function(d) {return (d)});
		  	selection.enter().append("circle")
			    .attr("class", "dot")
			    .attr("r", 3.5)
			    .attr("cx", xMap)
			    .attr("cy", yMap);
            selection.on("mouseover", function(d) {
            	$("#hovered").text(d[2]);
            });
			selection.exit().remove();
			svg.select(".x.axis")
                .transition()
                .duration(1000)
                .call(xAxis);
    	});
    d3.select('#sel-y')
    	.on('change', function() {
    		yVar = $('#sel-y option:selected').val();
    		dataset = subset(xVar, yVar);
    		console.log(xVar, yVar, dataset[0], dataset[0]);
    		yValue = function(d) { return d[1];};
			yScale = d3.scale.linear().range([height - padding, padding]);
			yMap = function (d) { return yScale(yValue(d))};
			yAxis = d3.svg.axis().scale(yScale).orient("left").ticks(5);
			yScale.domain([d3.min(dataset, yValue)-2, d3.max(dataset, yValue)+2]);
			var svg = d3.select('svg');
			var selection = svg.selectAll("circle").data(dataset, function(d) {return (d)});
			selection.enter().append("circle")
			    .attr("class", "dot")
			    .attr("r", 3.5)
			    .attr("cx", xMap)
			    .attr("cy", yMap);
            selection.on("mouseover", function(d) {
            	$("#hovered").text(d[2]);
            });
			selection.exit().remove();
			svg.select(".y.axis")
                .transition()
                .duration(1000)
                .call(yAxis);
    	});
    d3.select('#update')
    	.on('click', function() {
    		var min = + $('#mpg-min').val();
    		var max = + $('#mpg-max').val();
    		dataset = subset_min_max(xVar, yVar, min, max);
    		console.log(xVar, yVar, dataset[0], dataset[0]);
    		var svg = d3.select('svg');
			var selection = svg.selectAll("circle").data(dataset, function(d) {return (d)});
			selection.enter().append("circle")
			    .attr("class", "dot")
			    .attr("r", 3.5)
			    .attr("cx", xMap)
			    .attr("cy", yMap);
			selection.on("mouseover", function(d) {
				console.log('hello', d);
            	$("#hovered").text(d[2]);
            });
			selection.exit().remove();
    	})



}
