// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4:msg/EstimatorEventFlags.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__ESTIMATOR_EVENT_FLAGS__TRAITS_HPP_
#define PX4__MSG__DETAIL__ESTIMATOR_EVENT_FLAGS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4/msg/detail/estimator_event_flags__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4
{

namespace msg
{

inline void to_flow_style_yaml(
  const EstimatorEventFlags & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: timestamp_sample
  {
    out << "timestamp_sample: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_sample, out);
    out << ", ";
  }

  // member: information_event_changes
  {
    out << "information_event_changes: ";
    rosidl_generator_traits::value_to_yaml(msg.information_event_changes, out);
    out << ", ";
  }

  // member: gps_checks_passed
  {
    out << "gps_checks_passed: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_checks_passed, out);
    out << ", ";
  }

  // member: reset_vel_to_gps
  {
    out << "reset_vel_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_gps, out);
    out << ", ";
  }

  // member: reset_vel_to_flow
  {
    out << "reset_vel_to_flow: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_flow, out);
    out << ", ";
  }

  // member: reset_vel_to_vision
  {
    out << "reset_vel_to_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_vision, out);
    out << ", ";
  }

  // member: reset_vel_to_zero
  {
    out << "reset_vel_to_zero: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_zero, out);
    out << ", ";
  }

  // member: reset_pos_to_last_known
  {
    out << "reset_pos_to_last_known: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_last_known, out);
    out << ", ";
  }

  // member: reset_pos_to_gps
  {
    out << "reset_pos_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_gps, out);
    out << ", ";
  }

  // member: reset_pos_to_vision
  {
    out << "reset_pos_to_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_vision, out);
    out << ", ";
  }

  // member: starting_gps_fusion
  {
    out << "starting_gps_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_gps_fusion, out);
    out << ", ";
  }

  // member: starting_vision_pos_fusion
  {
    out << "starting_vision_pos_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_pos_fusion, out);
    out << ", ";
  }

  // member: starting_vision_vel_fusion
  {
    out << "starting_vision_vel_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_vel_fusion, out);
    out << ", ";
  }

  // member: starting_vision_yaw_fusion
  {
    out << "starting_vision_yaw_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_yaw_fusion, out);
    out << ", ";
  }

  // member: yaw_aligned_to_imu_gps
  {
    out << "yaw_aligned_to_imu_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_aligned_to_imu_gps, out);
    out << ", ";
  }

  // member: reset_hgt_to_baro
  {
    out << "reset_hgt_to_baro: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_baro, out);
    out << ", ";
  }

  // member: reset_hgt_to_gps
  {
    out << "reset_hgt_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_gps, out);
    out << ", ";
  }

  // member: reset_hgt_to_rng
  {
    out << "reset_hgt_to_rng: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_rng, out);
    out << ", ";
  }

  // member: reset_hgt_to_ev
  {
    out << "reset_hgt_to_ev: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_ev, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const EstimatorEventFlags & msg,
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

  // member: timestamp_sample
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp_sample: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_sample, out);
    out << "\n";
  }

  // member: information_event_changes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "information_event_changes: ";
    rosidl_generator_traits::value_to_yaml(msg.information_event_changes, out);
    out << "\n";
  }

  // member: gps_checks_passed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gps_checks_passed: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_checks_passed, out);
    out << "\n";
  }

  // member: reset_vel_to_gps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_vel_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_gps, out);
    out << "\n";
  }

  // member: reset_vel_to_flow
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_vel_to_flow: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_flow, out);
    out << "\n";
  }

  // member: reset_vel_to_vision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_vel_to_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_vision, out);
    out << "\n";
  }

  // member: reset_vel_to_zero
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_vel_to_zero: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_vel_to_zero, out);
    out << "\n";
  }

  // member: reset_pos_to_last_known
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_pos_to_last_known: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_last_known, out);
    out << "\n";
  }

  // member: reset_pos_to_gps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_pos_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_gps, out);
    out << "\n";
  }

  // member: reset_pos_to_vision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_pos_to_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_pos_to_vision, out);
    out << "\n";
  }

  // member: starting_gps_fusion
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_gps_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_gps_fusion, out);
    out << "\n";
  }

  // member: starting_vision_pos_fusion
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_vision_pos_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_pos_fusion, out);
    out << "\n";
  }

  // member: starting_vision_vel_fusion
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_vision_vel_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_vel_fusion, out);
    out << "\n";
  }

  // member: starting_vision_yaw_fusion
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "starting_vision_yaw_fusion: ";
    rosidl_generator_traits::value_to_yaml(msg.starting_vision_yaw_fusion, out);
    out << "\n";
  }

  // member: yaw_aligned_to_imu_gps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_aligned_to_imu_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_aligned_to_imu_gps, out);
    out << "\n";
  }

  // member: reset_hgt_to_baro
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_hgt_to_baro: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_baro, out);
    out << "\n";
  }

  // member: reset_hgt_to_gps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_hgt_to_gps: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_gps, out);
    out << "\n";
  }

  // member: reset_hgt_to_rng
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_hgt_to_rng: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_rng, out);
    out << "\n";
  }

  // member: reset_hgt_to_ev
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_hgt_to_ev: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_hgt_to_ev, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const EstimatorEventFlags & msg, bool use_flow_style = false)
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
  const px4::msg::EstimatorEventFlags & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4::msg::EstimatorEventFlags & msg)
{
  return px4::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4::msg::EstimatorEventFlags>()
{
  return "px4::msg::EstimatorEventFlags";
}

template<>
inline const char * name<px4::msg::EstimatorEventFlags>()
{
  return "px4/msg/EstimatorEventFlags";
}

template<>
struct has_fixed_size<px4::msg::EstimatorEventFlags>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4::msg::EstimatorEventFlags>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4::msg::EstimatorEventFlags>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4__MSG__DETAIL__ESTIMATOR_EVENT_FLAGS__TRAITS_HPP_
