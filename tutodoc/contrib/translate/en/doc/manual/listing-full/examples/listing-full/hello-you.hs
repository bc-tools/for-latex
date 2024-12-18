main :: IO ()

main = do
    putStr "Who are you? "
    name <- getLine

    if name == ""
        then putStrLn "Ah, not very chatty today!"

    else do
        putStrLn ("Hello " ++ name ++ ".")
        putStrLn "Amazing! Actually, not at all..."
