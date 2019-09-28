use std::env;
use std::mem;
use std::ptr;

fn main() {
    let args: Vec<String> = env::args().collect();

    // TODO: Match?
    let serial_number: i32 = args[1].parse().unwrap();

    // https://doc.rust-lang.org/nomicon/unchecked-uninit.html
    const WIDTH: usize = 300;
    const HEIGHT: usize = 300;
    const SIZE: usize = WIDTH * HEIGHT;

    let mut fuel_cells: [i32; SIZE];
    unsafe {
        fuel_cells = mem::uninitialized();
        for x in 0..WIDTH {
            for y in 0..HEIGHT {
                let rack_id: i32 = (x as i32) + 10;

                let mut power_level: i32 = rack_id * (y as i32);

                power_level += serial_number;

                power_level *= rack_id;

                power_level /= 100;

                power_level %= 10;

                power_level -= 5;

                ptr::write(&mut fuel_cells[x + y * WIDTH], power_level);
            }
        }
    }

    let mut max_x: usize = 0;
    let mut max_y: usize = 0;
    let mut max_size: usize = 0;
    let mut max_power: i32 = 0;
    for size in 3..301 {
        println!("{}", size);
        for x in 0..(WIDTH - size) {
            for y in 0..(HEIGHT - size) {
                let mut power_level: i32 = 0;

                for i in 0..size {
                    power_level += &fuel_cells[(x + (y + i) * WIDTH)..((x + size) + (y + i) * WIDTH)].into_iter().sum()
                }

                if power_level > max_power {
                    max_x = x;
                    max_y = y;
                    max_size = size;
                    max_power = power_level;

                    println!("Max power is {} at ({},{},{})", max_power, max_x, max_y, max_size);
                }
            }
        }
    }

    println!("Max power is {} at ({},{},{})", max_power, max_x, max_y, max_size);
}
