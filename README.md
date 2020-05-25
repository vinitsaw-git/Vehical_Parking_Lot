# Vehical_Parking_Lot

Nature of the Game
We want to understand how you think as a programmer, and the level of craft you bring
to bear when building software.
Rules of the Game
1. You have 3 hours to implement a solution.
2. We are really, really interested in your object oriented or functional design skills,
so please craft the most beautiful code you can.
3. We’re also interested in understanding how you make assumptions when
building software. If a particular workflow or boundary condition is not defined in
the problem statement below, what you do is your choice.
4. You have to solve the problem in any object oriented or functional
language without using any external libraries to the core language.
5. Please use Git for version control. We expect you to send us a standard zip or
tarball of your source code when you're done that includes Git metadata (the .git
folder) in the tarball so we can look at your commit logs and understand how your
solution evolved. Frequent commits are a huge plus. DO NOT PUSH IT TO
ORIGIN
6. Your codebase should have the same level of structure and organization as any
mature open source project including coding conventions, directory structure and
build approach (make, gradle etc) and a README.md with clear instructions.
7. Please do not search for the solution online as it would be really lame thing to do :)
Problem Statement
I own a parking lot that can hold up to 'n' cars at any given point in time. Each slot is
given a number starting at 1 increasing with increasing distance from the entry point in
steps of one. I want to create an automated ticketing system that allows my customers
to use my parking lot without human intervention.
When a car enters my parking lot, I want to have a ticket issued to the driver. The ticket
issuing process includes us documenting the registration number (number plate) and
the colour of the car and allocating an available parking slot to the car before actually
handing over a ticket to the driver (we assume that our customers are nice enough to
always park in the slots allocated to them). The customer should be allocated a parking
slot which is nearest to the entry. At the exit the customer returns the ticket which then
marks the slot they were using as being available.
Due to government regulation, the system should provide me with the ability to find out:
● Registration numbers of all cars of a particular colour.
● Slot number in which a car with a given registration number is parked.
● Slot numbers of all slots where a car of a particular colour is parked.
We interact with the system via a simple set of commands which produce a
specific output. Please take a look at the example below, which includes all the
commands you need to support - they're self explanatory. The system should
allow input in one way.
It should provide us with an interactive command prompt based shell
where commands can be typed in
Example: Interactive
To run the program and launch the shell:
Assuming a parking lot with 6 slots, the following commands should be run in sequence
by typing them in at a prompt and should produce output as described below the
command. Note that exit terminates the process and returns control to the shell.
$ create_parking_lot 6
Created a parking lot with 6 slots
$ park KA-01-HH-1234 White Allocated slot number: 1
$ park KA-01-HH-9999 White Allocated slot number: 2
$ park KA-01-BB-0001 Black Allocated slot number: 3
$ park KA-01-HH-7777 Red Allocated slot number: 4
$ park KA-01-HH-2701 Blue Allocated slot number: 5
$ park KA-01-HH-3141 Black Allocated slot number: 6
$ leave 4
Slot number 4 is free
$ park KA-01-P-333 White Allocated slot number: 4
$ park DL-12-AA-9999 White Sorry, parking lot is full
$ registration_numbers_for_cars_with_colour White KA-01-HH-1234,
KA-01-HH-9999, KA-01-P-333
$ slot_numbers_for_cars_with_colour White
1, 2, 4
$ slot_number_for_registration_number KA-01-HH-3141
6
$ slot_number_for_registration_number MH-04-AY-1111
Not found
$ exit
Command List to be supported
create_parking_lot
park
leave
status
registration_numbers_for_cars_with_colour
slot_numbers_for_cars_with_colour
exit
