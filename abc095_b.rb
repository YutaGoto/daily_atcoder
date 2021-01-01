n, x = gets.chomp.split(" ").map(&:to_i)

d = []

min = 1000

n.times do
  a = gets.to_i
  d.append(a)

  if min > a
    min = a
  end
end

puts ((x-d.sum()) / min) + n
