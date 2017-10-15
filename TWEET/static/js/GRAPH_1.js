							

							var svg = d3.select("svg"),
								margin = {top: 50	, right: 20, bottom: 50, left: 100},
								width = +svg.attr("width") - margin.left - margin.right,
								height = +svg.attr("height") - margin.top - margin.bottom;

							var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
								y = d3.scaleLinear().rangeRound([height, 0]);

							var g = svg.append("g")
								.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

							d3.tsv("{% static "data/ZIG.tsv" %}", function(d) {
							  d.MT = +d.MT;
							  return d;	
							}, function(error, data) {
							  if (error) throw error;

							  x.domain(data.map(function(d) { return d.KEY; }));
							  y.domain([0, d3.max(data, function(d) { return d.MT; })]);

							  g.append("g")
								  .attr("class", "axis axis--x")
								  .attr("transform", "translate(0," + height + ")")
								  .call(d3.axisBottom(x))
								  .selectAll("text") 
									.attr("dx", "-.8em")
									.attr("dy", "1.5em")
									.attr("transform", "rotate(-45)");

									  //Create X axis label   
							  g.append("text")
									.attr("x", width / 2 )
									.attr("y",  height + margin.bottom)
									.style("text-anchor", "middle")
									.text("Date")
									.attr("font-size",  "20px")
									.attr("font-family",  "Calibri")
									;  

							  g.append("text")
									.attr("x", width / 2)
									.attr("y",  -25)
									.style("text-anchor", "middle")
									.text("CA Mensuel")
									.attr("font-size",  "20px")
									.attr("font-family",  "Calibri")
									;  

							  g.append("g")
								  .attr("class", "axis axis--y")
								  .call(d3.axisLeft(y).ticks(5))
								.append("text")
								  .attr("transform", "rotate(-90)")
								  .attr("y", 6)
								  .attr("dy", ".2em")
								  .attr("text-anchor", "end")
								  .text("MT");
								
							  g.append("text")	
									.attr("x",  -70)
									.attr("y",  height/2)
									.style("text-anchor", "middle")
									.text("CA")
									.attr("font-size",  "20px")
									.attr("font-family",  "Calibri")
									;  
								
												
							  g.selectAll(".bar")
								.data(data)
								.enter().append("rect")
								  .attr("class", "bar")
								  .attr("x", function(d) { return x(d.KEY); })
								  .attr("y", function(d) { return y(d.MT); })
								  .attr("width", x.bandwidth())
								  .attr("height", function(d) { return height - y(d.MT); });
								  

							});

							