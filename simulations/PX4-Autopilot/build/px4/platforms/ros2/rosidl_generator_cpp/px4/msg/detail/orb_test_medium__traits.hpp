// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4:msg/OrbTestMedium.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__ORB_TEST_MEDIUM__TRAITS_HPP_
#define PX4__MSG__DETAIL__ORB_TEST_MEDIUM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4/msg/detail/orb_test_medium__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4
{

namespace msg
{

inline void to_flow_style_yaml(
  const OrbTestMedium & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: val
  {
    out << "val: ";
    rosidl_generator_traits::value_to_yaml(msg.val, out);
    out << ", ";
  }

  // member: junk
  {
    if (msg.junk.size() == 0) {
      out << "junk: []";
    } else {
      out << "junk: [";
      size_t pending_items = msg.junk.size();
      for (auto item : msg.junk) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OrbTestMedium & msg,
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

  // member: val
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "val: ";
    rosidl_generator_traits::value_to_yaml(msg.val, out);
    out << "\n";
  }

  // member: junk
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.junk.size() == 0) {
      out << "junk: []\n";
    } else {
      out << "junk:\n";
      for (auto item : msg.junk) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OrbTestMedium & msg, bool use_flow_style = false)
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
  const px4::msg::OrbTestMedium & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4::msg::OrbTestMedium & msg)
{
  return px4::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4::msg::OrbTestMedium>()
{
  return "px4::msg::OrbTestMedium";
}

template<>
inline const char * name<px4::msg::OrbTestMedium>()
{
  return "px4/msg/OrbTestMedium";
}

template<>
struct has_fixed_size<px4::msg::OrbTestMedium>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4::msg::OrbTestMedium>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4::msg::OrbTestMedium>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4__MSG__DETAIL__ORB_TEST_MEDIUM__TRAITS_HPP_
