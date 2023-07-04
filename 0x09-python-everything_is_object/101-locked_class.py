#!/usr/bin/python3
"""Desines a locked class."""


class Locked Class:
    """
    prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
