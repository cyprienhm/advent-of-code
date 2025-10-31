

sliding :: Int -> [a] -> [[a]]
sliding n l | length  l < n = []
            | otherwise  = take n l : sliding n (tail l)

main :: IO ()
main = do
    contents <- readFile "./input.txt"
    let numbersStr = takeWhile (/= "") (lines contents)
    let numbers = map read numbersStr :: [Integer]
    let tuples = sliding 3 numbers
    let sums = map sum tuples

    let sumPairs = sliding 2 sums
    let comparePair running [x,y] | x < y = running+1
                                  | otherwise  = running

    let result = foldl comparePair 0 sumPairs
    print result
