function instr_to_amount(instr)
  amount = parse(Int, instr[2:end])
  if instr[1] == 'L'
    return -amount
  else
    return amount
  end
end

data = read("./input.txt", String) |> split .|> instr_to_amount

function part1()
  pos = 50
  count = 0
  for n in data
    pos = (pos+n) % 100
    count += pos==0
  end
  return count
end

function part2()
  pos = 50
  count = 0
  for n in data
    for _=1:abs(n)
      pos += sign(n)
      count += pos==0
      if pos < 0
        pos += 100
      end
      if pos == 100
        pos -= 100
        count += 1
      end
    end
    # println(pos, " - ", count)
  end
  return count
end

println(part1())
println(part2())
