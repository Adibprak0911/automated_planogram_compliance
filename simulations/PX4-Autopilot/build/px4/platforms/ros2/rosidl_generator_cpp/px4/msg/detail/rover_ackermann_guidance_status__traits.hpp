// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4:msg/RoverAckermannGuidanceStatus.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__TRAITS_HPP_
#define PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4/msg/detail/rover_ackermann_guidance_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4
{

namespace msg
{

inline void to_flow_style_yaml(
  const RoverAckermannGuidanceStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: desired_speed
  {
    out << "desired_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.desired_speed, out);
    out << ", ";
  }

  // member: lookahead_distance
  {
    out << "lookahead_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.lookahead_distance, out);
    out << ", ";
  }

  // member: heading_error
  {
    out << "heading_error: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_error, out);
    out << ", ";
  }

  // member: pid_throttle_integral
  {
    out << "pid_throttle_integral: ";
    rosidl_generator_traits::value_to_yaml(msg.pid_throttle_integral, out);
    out << ", ";
  }

  // member: crosstrack_error
  {
    out << "crosstrack_error: ";
    rosidl_generator_traits::value_to_yaml(msg.crosstrack_error, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RoverAckermannGuidanceStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << "\n";
  }

  // member: desired_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "desired_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.desired_speed, out);
    out << "\n";
  }

  // member: lookahead_distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lookahead_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.lookahead_distance, out);
    out << "\n";
  }

  // member: heading_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "heading_error: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_error, out);
    out << "\n";
  }

  // member: pid_throttle_integral
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pid_throttle_integral: ";
    rosidl_generator_traits::value_to_yaml(msg.pid_throttle_integral, out);
    out << "\n";
  }

  // member: crosstrack_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "crosstrack_error: ";
    rosidl_generator_traits::value_to_yaml(msg.crosstrack_error, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RoverAckermannGuidanceStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace px4

namespace rosidl_generator_traits
{

[[deprecated("use px4::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const px4::msg::RoverAckermannGuidanceStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4::msg::RoverAckermannGuidanceStatus & msg)
{
  return px4::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4::msg::RoverAckermannGuidanceStatus>()
{
  return "px4::msg::RoverAckermannGuidanceStatus";
}

template<>
inline const char * name<px4::msg::RoverAckermannGuidanceStatus>()
{
  return "px4/msg/RoverAckermannGuidanceStatus";
}

template<>
struct has_fixed_size<px4::msg::RoverAckermannGuidanceStatus>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4::msg::RoverAckermannGuidanceStatus>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4::msg::RoverAckermannGuidanceStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4__MSG__DETAIL__ROVER_ACKERMANN_GUIDANCE_STATUS__TRAITS_HPP_
