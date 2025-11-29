function y_contains_x(x, y)
   return x[1] >= y[1] && x[2] <= y[2]
end

function part1(filename)
  data = read(filename, String)
  data = split(strip(data), "\n")
  data = map(pairs->map(ranges->map(elt->parse(Int, elt), split(ranges,"-")),split(pairs, ",")), data)
  res = sum(map(x->y_contains_x(x[1],x[2]) || y_contains_x(x[2],x[1]), data))
  return res
end


function overlaps(x,y)
  return (y_contains_x(x,y) || y_contains_x(y,x) || x[2] >= y[1] || y[2] >= x[1]) && !(x[2] < y[1] || y[2] < x[1]) 
end

function part2(filename)
  data = read(filename, String)
  data = split(strip(data), "\n")
  data = map(pairs->map(ranges->map(elt->parse(Int, elt), split(ranges,"-")),split(pairs, ",")), data)
  res = sum(map(x->overlaps(x[1],x[2]), data))
  return res
end

filename = "input.txt"
println(part1(filename))
println(part2(filename))
