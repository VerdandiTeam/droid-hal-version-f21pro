# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device f21pro
%define vendor duoqin

# Manufacturer and device name to be shown in UI
%define vendor_pretty Qin
%define device_pretty F21 Pro

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1

BuildRequires: droid-hal-%{device}
BuildRequires: droid-hal-%{device}-img-boot
BuildRequires: droid-hal-%{device}-img-recovery
BuildRequires: droid-hal-%{device}-kernel
BuildRequires: droid-hal-%{device}-tools
BuildRequires: droid-hal-%{device}-kernel-dtbo

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

