n, d = gets.chomp.split(" ").map(&:to_i)
points = []
intcount = 0

n.times do
  point = gets.chomp.split(" ").map(&:to_i)
  points.push(point)
end

points.combination(2).each do |pnt|
  distance = 0
  d.times do |i|
    distance += (pnt[0][i] - pnt[1][i])**2
  end
  distance = Math.sqrt(distance)
  if distance.to_i == distance
    intcount += 1
  end
end

puts intcount
