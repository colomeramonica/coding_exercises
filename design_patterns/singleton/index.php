<?php

require_once './HotelGuests.php';
require_once './KittyHotel.php';

$miley = new HotelGuests('Miley', 'frajola', '12');
$kimiko = new HotelGuests('Kimiko', 'tricolor', '1');
$amora = new HotelGuests('Amora', 'siberiana', '3');

$kittyHotel = KittyHotel::getInstance();
$kittyHotel->setGuests([$miley, $kimiko, $amora]);

echo ("\n\nHóspedes\n\n");
var_dump($kittyHotel);