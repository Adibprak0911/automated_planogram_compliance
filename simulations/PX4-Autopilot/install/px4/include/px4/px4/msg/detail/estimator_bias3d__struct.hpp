// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4:msg/EstimatorBias3d.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__ESTIMATOR_BIAS3D__STRUCT_HPP_
#define PX4__MSG__DETAIL__ESTIMATOR_BIAS3D__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4__msg__EstimatorBias3d __attribute__((deprecated))
#else
# define DEPRECATED__px4__msg__EstimatorBias3d __declspec(deprecated)
#endif

namespace px4
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct EstimatorBias3d_
{
  using Type = EstimatorBias3d_<ContainerAllocator>;

  explicit EstimatorBias3d_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_sample = 0ull;
      this->device_id = 0ul;
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias.begin(), this->bias.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias_var.begin(), this->bias_var.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov.begin(), this->innov.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov_var.begin(), this->innov_var.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov_test_ratio.begin(), this->innov_test_ratio.end(), 0.0f);
    }
  }

  explicit EstimatorBias3d_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : bias(_alloc),
    bias_var(_alloc),
    innov(_alloc),
    innov_var(_alloc),
    innov_test_ratio(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_sample = 0ull;
      this->device_id = 0ul;
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias.begin(), this->bias.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias_var.begin(), this->bias_var.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov.begin(), this->innov.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov_var.begin(), this->innov_var.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->innov_test_ratio.begin(), this->innov_test_ratio.end(), 0.0f);
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _timestamp_sample_type =
    uint64_t;
  _timestamp_sample_type timestamp_sample;
  using _device_id_type =
    uint32_t;
  _device_id_type device_id;
  using _bias_type =
    std::array<float, 3>;
  _bias_type bias;
  using _bias_var_type =
    std::array<float, 3>;
  _bias_var_type bias_var;
  using _innov_type =
    std::array<float, 3>;
  _innov_type innov;
  using _innov_var_type =
    std::array<float, 3>;
  _innov_var_type innov_var;
  using _innov_test_ratio_type =
    std::array<float, 3>;
  _innov_test_ratio_type innov_test_ratio;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__timestamp_sample(
    const uint64_t & _arg)
  {
    this->timestamp_sample = _arg;
    return *this;
  }
  Type & set__device_id(
    const uint32_t & _arg)
  {
    this->device_id = _arg;
    return *this;
  }
  Type & set__bias(
    const std::array<float, 3> & _arg)
  {
    this->bias = _arg;
    return *this;
  }
  Type & set__bias_var(
    const std::array<float, 3> & _arg)
  {
    this->bias_var = _arg;
    return *this;
  }
  Type & set__innov(
    const std::array<float, 3> & _arg)
  {
    this->innov = _arg;
    return *this;
  }
  Type & set__innov_var(
    const std::array<float, 3> & _arg)
  {
    this->innov_var = _arg;
    return *this;
  }
  Type & set__innov_test_ratio(
    const std::array<float, 3> & _arg)
  {
    this->innov_test_ratio = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4::msg::EstimatorBias3d_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4::msg::EstimatorBias3d_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4::msg::EstimatorBias3d_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4::msg::EstimatorBias3d_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4__msg__EstimatorBias3d
    std::shared_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4__msg__EstimatorBias3d
    std::shared_ptr<px4::msg::EstimatorBias3d_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EstimatorBias3d_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->timestamp_sample != other.timestamp_sample) {
      return false;
    }
    if (this->device_id != other.device_id) {
      return false;
    }
    if (this->bias != other.bias) {
      return false;
    }
    if (this->bias_var != other.bias_var) {
      return false;
    }
    if (this->innov != other.innov) {
      return false;
    }
    if (this->innov_var != other.innov_var) {
      return false;
    }
    if (this->innov_test_ratio != other.innov_test_ratio) {
      return false;
    }
    return true;
  }
  bool operator!=(const EstimatorBias3d_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EstimatorBias3d_

// alias to use template instance with default allocator
using EstimatorBias3d =
  px4::msg::EstimatorBias3d_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4

#endif  // PX4__MSG__DETAIL__ESTIMATOR_BIAS3D__STRUCT_HPP_
