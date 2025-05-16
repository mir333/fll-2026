import orientation
from hub import motion_sensor
from hub import port
import runloop
import motor_pair
import motor
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

kp = -5
async def goforward(vzdalenost, speed):
    motion_sensor.reset_yaw(0)
    pozice = 0
    motor.reset_relative_position(port.A, 0)
    motor.reset_relative_position(port.B, 0)
    await runloop.sleep_ms(50)
    while vzdalenost > pozice * -1:
        motorcorrection = (motion_sensor.tilt_angles()[0] * kp)
        pozice = motor.relative_position(port.A) * + motor.relative_position(port.B) /720 * 17.6
        motor.set_duty_cycle(port.A, speed + motorcorrection)
        motor.set_duty_cycle(port.B, (speed - motorcorrection ) * -1)
        print(motorcorrection)
        await runloop.sleep_ms(100)
    motor.stop(port.A)
    motor.stop(port.B)



async def main():
    await goforward(100000, 10000)
    motion_sensor.reset_yaw(0)
    print(motor.relative_position(port.A) + motor.relative_position(port.B))
    while False:
        print(motion_sensor.tilt_angles()[0])
        await runloop.sleep_ms(200)
runloop.run(main())
