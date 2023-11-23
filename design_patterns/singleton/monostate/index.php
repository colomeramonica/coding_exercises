<?php

require_once '../HotelGuests.php';
require_once './KittyHotel.php';

$miley = new HotelGuests('Miley', 'frajola', '12');
$kimiko = new HotelGuests('Kimiko', 'tricolor', '1');
$amora = new HotelGuests('Amora', 'siberiana', '3');

$kittyHotel = new KittyHotel;
$kittyHotel->setGuests([$miley]);

$kittyHotel2 = new KittyHotel;
$kittyHotel2->setGuests([$kimiko, $amora]);

echo ("\n\nHóspedes\n\n");
var_dump($kittyHotel);

echo ("\n\nHóspedes 2\n\n");
var_dump($kittyHotel2);