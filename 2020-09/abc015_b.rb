n = gets.to_i
arr = gets.chomp.split(" ").map(&:to_i)

print (arr.sum / (n - arr.count(0)).to_f).ceil
