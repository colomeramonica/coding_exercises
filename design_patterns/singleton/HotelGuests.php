<?php

class HotelGuests {
    public $name;
    public $breed;
    public $age;

    public function __construct($name, $breed, $age) {
        $this->name = $name;
        $this->breed = $breed;
        $this->age = $age;
    }
}