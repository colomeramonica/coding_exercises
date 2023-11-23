<?php

class KittyHotel {
    private static $guests = [];

    public function __constructor() {}

    public function setGuests($guests) {
        self::$guests = array_merge(self::$guests, $guests);
    }

    public function getGuests() {
        return self::guests;
    }
}