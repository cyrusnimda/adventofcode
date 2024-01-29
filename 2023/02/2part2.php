<?php

$live = [
    "5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 19 blue; 1 red, 17 blue",
    "4 red, 5 green, 2 blue; 7 red, 14 green, 3 blue; 2 green, 5 blue, 11 red; 10 blue, 3 green; 9 green, 6 blue, 13 red; 7 red, 5 green, 9 blue",
    "9 green, 18 blue, 1 red; 6 red, 10 blue, 5 green; 4 blue, 4 red, 15 green",
    "1 red, 13 green; 10 green, 2 red; 3 red, 4 green, 2 blue",
    "4 red, 2 green, 1 blue; 4 red, 9 blue; 4 green, 1 red, 6 blue; 3 blue, 2 green, 6 red; 5 red, 4 green, 1 blue",
    "6 red, 3 green, 6 blue; 3 green, 5 blue, 12 red; 3 green, 9 blue, 3 red; 13 red, 8 blue",
    "3 blue, 1 red; 3 blue, 10 green; 4 green, 5 blue",
    "11 green, 4 blue; 4 red, 4 blue, 11 green; 4 green, 3 blue; 1 blue, 6 red, 12 green",
    "1 blue, 4 green, 1 red; 5 green, 3 blue; 9 green, 4 blue; 3 blue, 1 red, 10 green; 6 green, 2 blue",
    "5 green, 6 red, 7 blue; 7 green, 5 blue, 5 red; 8 red, 6 blue, 8 green; 2 blue, 8 green, 6 red; 6 blue, 8 red, 4 green",
    "1 blue, 10 red, 10 green; 11 green, 2 blue, 16 red; 4 blue, 7 red, 14 green",
    "8 green, 9 red, 12 blue; 2 green, 4 blue, 7 red; 1 red, 9 blue, 7 green; 8 green, 2 red, 10 blue; 1 green, 5 red, 5 blue; 6 green, 5 red, 1 blue",
    "3 green, 1 blue, 6 red; 1 green, 10 red; 1 blue, 15 red, 2 green",
    "2 green, 6 blue; 1 green, 2 blue, 2 red; 5 blue, 1 green, 2 red; 4 green, 5 blue, 4 red; 4 red, 5 green, 4 blue; 1 red, 5 green, 6 blue",
    "12 green, 7 blue; 19 green; 11 blue, 16 green, 1 red; 1 red, 2 green, 3 blue; 8 blue, 1 red, 19 green; 14 blue, 3 green, 1 red",
    "2 green, 13 blue, 3 red; 5 red, 12 blue; 6 blue, 8 red; 4 red, 1 green, 4 blue; 1 green, 15 blue; 4 blue, 2 green, 1 red",
    "11 blue, 7 green, 2 red; 12 red, 8 green, 8 blue; 2 red, 6 blue, 6 green",
    "1 green, 2 blue; 2 green, 1 blue, 4 red; 3 green, 16 red; 2 red, 3 green",
    "11 blue, 3 green, 3 red; 11 blue, 5 green; 3 green, 3 red, 8 blue",
    "1 green, 6 blue; 4 blue, 6 green; 1 red, 10 green; 12 green; 5 blue, 1 red, 4 green; 1 green, 5 blue",
    "7 green, 3 blue; 1 red, 5 blue, 6 green; 1 red, 11 green; 8 blue, 1 red, 10 green; 1 red, 5 blue, 3 green",
    "3 red, 1 blue; 3 green, 1 red, 1 blue; 7 green, 2 blue",
    "12 green, 1 red, 2 blue; 10 blue, 1 green, 1 red; 9 blue, 8 green",
    "5 blue, 6 green, 6 red; 3 blue, 1 red; 8 blue, 2 green, 12 red; 1 green, 2 blue, 14 red; 2 blue, 5 green, 15 red",
    "6 red, 13 green; 1 blue, 1 red, 3 green; 1 blue, 12 red, 10 green",
    "16 red, 2 blue, 7 green; 1 blue, 7 green, 8 red; 1 blue, 3 red, 9 green",
    "4 blue, 15 green; 6 green, 2 blue, 1 red; 9 blue, 10 green, 4 red; 3 red, 3 green, 6 blue; 11 blue, 7 red, 11 green; 6 red, 5 green, 13 blue",
    "10 blue, 8 red, 10 green; 4 blue, 11 red, 6 green; 8 red, 9 green, 10 blue; 4 red, 9 green, 2 blue",
    "4 red, 9 green, 7 blue; 10 blue, 6 green, 4 red; 1 green, 2 red, 10 blue; 3 green, 9 blue",
    "6 blue, 9 green, 10 red; 6 blue, 4 red; 5 green, 2 blue; 5 green, 2 red, 2 blue; 6 blue, 8 green",
    "7 blue; 2 green, 6 blue; 1 red, 9 blue, 5 green",
    "8 blue, 2 red, 4 green; 6 red, 2 blue, 1 green; 14 blue, 8 green, 8 red",
    "1 green, 1 red, 1 blue; 2 blue, 1 green, 12 red; 1 green, 1 red; 1 blue, 2 red, 1 green; 7 red, 2 green, 2 blue",
    "3 blue; 2 blue; 10 red, 1 blue, 1 green; 5 red; 1 green, 1 red, 1 blue; 1 green, 2 red",
    "10 green, 1 red, 16 blue; 4 red, 10 blue, 9 green; 1 green, 7 blue, 5 red",
    "1 blue, 3 red, 16 green; 1 blue, 3 red, 1 green; 9 green, 3 red, 8 blue; 14 green, 6 blue, 3 red; 3 red, 12 green, 4 blue",
    "11 red, 3 blue; 15 red, 8 blue, 6 green; 6 green, 19 red, 11 blue; 1 green, 4 blue, 14 red; 12 blue, 5 red, 8 green; 4 blue, 9 red",
    "4 green, 10 blue, 3 red; 1 green, 1 red, 11 blue; 2 red, 12 blue",
    "3 green, 1 red, 4 blue; 9 green, 1 red, 18 blue; 4 red, 4 green, 17 blue; 4 red, 10 blue, 14 green",
    "5 red, 4 green, 8 blue; 1 green, 9 blue; 9 blue, 3 red, 6 green; 8 red, 9 blue, 9 green",
    "1 blue, 9 red, 3 green; 9 red, 10 green, 15 blue; 13 red, 8 green, 8 blue; 19 red, 6 blue, 2 green; 7 green, 5 blue, 12 red",
    "15 blue; 1 red, 1 green, 9 blue; 6 blue, 1 red; 1 green, 4 blue",
    "1 green, 8 blue, 2 red; 1 red, 1 green, 6 blue; 7 blue; 7 blue, 3 red, 1 green; 2 red, 5 blue",
    "7 green, 11 blue, 6 red; 9 green, 8 blue; 4 red, 15 green; 12 green, 14 blue, 8 red",
    "4 red, 4 green; 14 green; 4 green, 2 blue; 1 blue, 12 red, 5 green; 3 red, 6 green; 11 red, 1 green",
    "2 blue, 1 green, 1 red; 1 blue, 6 green, 1 red; 2 blue, 1 red, 1 green; 5 green",
    "1 blue, 1 red; 14 red; 3 green, 2 blue, 17 red; 4 green",
    "1 red, 11 green, 2 blue; 1 red, 11 green, 6 blue; 13 green, 1 blue, 3 red; 3 green, 4 red, 6 blue; 12 green, 5 blue, 1 red; 2 red, 4 green, 4 blue",
    "5 blue, 3 green; 2 green, 8 blue; 5 blue; 4 green, 5 blue, 1 red; 4 green, 7 blue; 1 green, 3 blue",
    "3 red, 5 green, 2 blue; 9 green, 7 red, 4 blue; 3 blue, 6 red, 13 green; 6 blue, 8 red, 9 green",
    "2 green, 11 red, 7 blue; 5 blue, 13 red; 1 green, 2 blue, 3 red; 6 blue, 8 red; 11 red, 2 green, 4 blue",
    "15 blue, 1 green, 4 red; 4 green, 10 blue, 2 red; 6 red, 18 blue, 1 green",
    "2 red, 10 green, 6 blue; 4 green, 3 blue, 3 red; 17 blue, 19 green, 5 red; 6 blue, 6 green, 9 red; 5 blue, 17 green, 7 red",
    "9 blue, 8 red, 6 green; 6 red, 8 green; 1 green, 6 blue, 1 red; 5 red, 4 green, 9 blue; 5 blue, 2 green, 5 red",
    "8 blue, 8 red, 10 green; 3 red, 4 green, 9 blue; 4 red, 3 green, 7 blue",
    "3 red, 6 green, 1 blue; 5 green, 1 blue, 1 red; 1 red, 2 green; 10 green",
    "1 green, 4 blue, 12 red; 17 red, 7 blue, 10 green; 17 red, 5 blue, 3 green",
    "1 red, 5 green, 14 blue; 5 green, 6 red, 7 blue; 4 blue, 8 green; 3 red, 9 green, 7 blue; 8 blue, 8 green, 6 red; 8 green, 7 blue, 5 red",
    "3 green, 5 red; 2 red, 13 green, 1 blue; 19 green, 1 red, 1 blue; 19 green, 1 blue; 18 green, 1 blue, 5 red; 6 red, 9 green",
    "5 red, 1 green, 6 blue; 8 red, 6 blue, 14 green; 8 green, 8 red, 3 blue; 2 blue, 5 green, 3 red; 4 blue, 1 red, 14 green",
    "7 red, 4 blue, 2 green; 2 green, 8 red, 9 blue; 5 blue, 2 green, 8 red; 8 red, 1 green, 8 blue",
    "6 red, 3 blue; 1 blue, 2 red, 2 green; 3 red, 1 blue",
    "2 red, 1 blue, 2 green; 1 blue, 1 green; 2 green, 4 red; 3 green, 2 red; 2 green",
    "5 green, 6 blue, 7 red; 2 red, 5 green, 8 blue; 7 green, 9 blue, 1 red; 4 green, 5 blue; 19 blue, 5 green, 13 red",
    "3 red, 1 blue, 4 green; 5 green, 3 blue; 9 green, 1 red, 10 blue",
    "6 red, 13 green, 2 blue; 2 blue, 5 red, 9 green; 18 red; 2 green, 1 blue, 1 red; 19 red, 10 green; 1 blue, 15 green, 13 red",
    "8 blue, 3 red; 1 red, 12 green, 7 blue; 4 red, 6 blue, 5 green; 11 green, 10 blue, 7 red; 5 red, 9 green, 14 blue",
    "1 red, 3 green; 10 blue, 1 red, 3 green; 1 green, 17 blue; 16 blue; 6 blue",
    "11 green, 5 blue, 8 red; 2 red, 5 green, 1 blue; 10 green, 2 blue; 11 green, 7 red, 4 blue",
    "2 green, 1 blue, 13 red; 16 green, 20 red, 4 blue; 10 red",
    "10 blue, 6 green, 7 red; 5 red, 5 green, 2 blue; 7 green, 4 red, 5 blue; 1 red, 8 blue; 5 red, 1 blue, 8 green; 5 blue, 1 red, 5 green",
    "2 red, 4 green; 2 green, 2 red, 1 blue; 3 blue, 3 green, 2 red; 2 green",
    "5 red, 19 blue; 12 blue, 4 green, 16 red; 14 red, 11 blue, 1 green",
    "2 red, 1 green, 9 blue; 5 blue, 1 green, 2 red; 2 green, 1 red, 13 blue; 2 green, 1 red, 3 blue",
    "7 blue, 1 red, 18 green; 17 green, 8 red, 13 blue; 15 blue, 4 red",
    "1 green, 12 red, 13 blue; 5 green, 11 blue, 12 red; 10 red, 1 green; 10 red, 2 blue; 5 red, 2 green; 2 green, 17 blue, 3 red",
    "2 blue, 1 red, 1 green; 7 red; 7 red, 3 blue, 2 green; 10 green, 1 red; 3 red, 7 blue, 6 green",
    "10 red, 2 blue, 2 green; 1 blue, 6 red, 4 green; 12 red, 8 green; 6 green, 8 red, 7 blue; 11 green, 5 blue, 6 red",
    "7 green, 5 red; 6 blue, 2 green, 15 red; 9 blue, 2 red, 12 green; 1 blue, 4 red, 10 green; 4 blue, 12 green, 11 red; 5 green, 3 red, 5 blue",
    "1 green, 13 blue, 2 red; 2 red, 1 green, 13 blue; 7 blue, 8 red",
    "1 green, 2 red, 11 blue; 5 red, 3 blue; 1 green, 1 red; 14 red, 1 green",
    "12 red, 3 blue, 8 green; 15 red, 9 blue, 8 green; 6 blue, 13 red, 8 green",
    "4 blue, 6 green, 3 red; 7 red, 2 blue, 9 green; 6 green, 3 red",
    "4 green; 3 red, 3 blue; 4 red, 1 blue, 2 green; 1 red, 5 green, 5 blue; 1 red, 5 blue, 3 green",
    "3 red, 4 blue, 15 green; 9 green; 2 red, 4 blue, 6 green; 1 red, 4 green, 7 blue; 3 red, 10 green, 9 blue; 1 red, 13 green, 3 blue",
    "8 red, 6 blue; 3 blue, 3 green, 15 red; 12 red, 6 green, 13 blue; 15 red, 6 green, 10 blue",
    "4 red, 4 blue; 6 red, 2 blue; 5 blue, 3 green; 4 blue, 2 red",
    "4 blue, 7 green; 2 blue, 7 green; 6 green, 4 blue; 1 red, 1 blue, 2 green; 11 green, 3 blue",
    "1 blue, 12 green, 11 red; 3 red, 7 blue, 1 green; 7 green, 8 red; 6 blue, 2 green, 3 red; 7 red, 8 green; 11 blue, 5 red, 12 green",
    "1 green, 12 red, 17 blue; 14 red, 17 blue, 9 green; 6 green, 9 red, 11 blue",
    "3 green, 14 blue; 2 blue, 2 green, 6 red; 1 red, 11 blue, 1 green; 3 green, 4 red, 20 blue; 6 red, 2 green, 3 blue; 10 blue, 12 red",
    "6 blue, 7 red; 2 blue, 4 red, 1 green; 4 red, 1 green, 3 blue; 2 red, 5 blue; 8 red, 6 blue; 1 green, 2 blue, 1 red",
    "4 blue, 1 green, 4 red; 8 red, 4 green, 4 blue; 2 blue, 9 red; 1 blue, 4 red; 4 blue, 2 green, 11 red",
    "5 blue, 1 green, 7 red; 1 green, 11 blue, 1 red; 1 green, 15 blue, 4 red",
    "1 red, 3 blue; 1 red, 1 green, 8 blue; 3 red, 1 green, 3 blue; 3 red, 6 blue; 6 blue",
    "4 green, 1 blue; 7 green, 3 red; 2 blue, 9 red, 16 green; 3 blue, 4 red, 11 green",
    "6 green, 8 blue; 1 blue, 1 green; 3 green, 4 blue; 8 blue, 5 green, 2 red",
    "18 blue, 6 green; 11 green, 3 blue, 7 red; 18 blue, 3 red, 7 green; 5 red, 5 green; 8 blue, 2 green, 11 red",
    "3 red, 2 green, 3 blue; 1 red, 4 green, 1 blue; 2 green, 18 red; 15 red, 1 blue; 2 blue, 9 red, 2 green; 17 red, 3 blue, 4 green",
    "9 blue, 8 red, 16 green; 3 red, 7 green, 8 blue; 1 green, 3 red, 12 blue; 3 green, 14 blue",
];

$test = [
    "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
];

function getSetsFromGames(string $game): array
{
    $sets = explode("; ", $game);
    $sets = array_map(function ($set) {
        $set = explode(", ", $set);
        $set = array_map(function ($cube) {
            $cube = explode(" ", $cube);
            return [
                "color" => $cube[1],
                "count" => $cube[0],
            ];
        }, $set);

        return $set;
    }, $sets);
    return $sets;
}

function getPowerFromGames(array $games): int
{
    $powerInGames = [];
    foreach ($games as $game) {
        $min_cubes_needed = [
            "red"   => 0,
            "green" => 0,
            "blue"  => 0,
        ];

        $sets = getSetsFromGames($game);
        //print_r($sets);
        foreach ($sets as $set) {
            foreach ($set as $hand) {
                if ($min_cubes_needed[$hand["color"]] < $hand["count"]) {
                    $min_cubes_needed[$hand["color"]] = $hand["count"];
                }
            }
        }
        $powerInGames[] = $min_cubes_needed["red"] * $min_cubes_needed["green"] * $min_cubes_needed["blue"];
        // print_r($min_cubes_needed);
        // print_r($powerInGames);
        // die;
    }

    $power = array_sum($powerInGames);
    return $power;
}

# Test should be 8
//print(getPowerFromGames($test));
print(getPowerFromGames($live));
