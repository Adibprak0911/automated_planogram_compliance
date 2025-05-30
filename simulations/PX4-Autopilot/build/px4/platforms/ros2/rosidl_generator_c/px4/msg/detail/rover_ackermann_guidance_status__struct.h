// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4:msg/RoverAckermannGuidanceStatus.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__STRUCT_H_
#define PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/RoverAckermannGuidanceStatus in the package px4.
typedef struct px4__msg__RoverAckermannGuidanceStatus
{
  /// time since system start (microseconds)
  uint64_t timestamp;
  /// Rover desired ground speed
  float desired_speed;
  /// Lookahead distance of pure the pursuit controller
  float lookahead_distance;
  /// Heading error of the pure pursuit controller
  float heading_error;
  /// [-1, 1] Integral of the PID for the normalized throttle to control the rover speed during missions
  float pid_throttle_integral;
  /// Shortest distance from the vehicle to the path
  float crosstrack_error;
} px4__msg__RoverAckermannGuidanceStatus;

// Struct for a sequence of px4__msg__RoverAckermannGuidanceStatus.
typedef struct px4__msg__RoverAckermannGuidanceStatus__Sequence
{
  px4__msg__RoverAckermannGuidanceStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4__msg__RoverAckermannGuidanceStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__STRUCT_H_
