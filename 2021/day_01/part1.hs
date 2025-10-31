main :: IO ()
main = do
    contents <- readFile "./input.txt"
    let numbersStr = takeWhile (/= "") (lines contents)
    let numbers = map read numbersStr :: [Integer]
    let pairs = zip numbers (tail numbers)
    let comparePair acc (x, y) | x < y = acc + 1  | otherwise = acc

    let result = foldl comparePair 0 pairs

    print result
