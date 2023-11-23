<?php

class KittyHotel {
    protected static $instance;
    private $guests = [];

    private function __constructor() {}
    private function __clone() {}
    private function __wakeup() {}

    public static function getInstance(): self {
        if (empty(self::$instance)) {
            self::$instance = new self();
        }

        return self::$instance;
    }

    public function setGuests($guests) {
        $this->guests = array_merge($this->guests, $guests);
    }
}