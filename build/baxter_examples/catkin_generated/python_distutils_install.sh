#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/eloise/catkin-ws/src/baxter_examples"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/eloise/catkin-ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/eloise/catkin-ws/install/lib/python2.7/dist-packages:/home/eloise/catkin-ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/eloise/catkin-ws/build" \
    "/usr/bin/python" \
    "/home/eloise/catkin-ws/src/baxter_examples/setup.py" \
    build --build-base "/home/eloise/catkin-ws/build/baxter_examples" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/eloise/catkin-ws/install" --install-scripts="/home/eloise/catkin-ws/install/bin"
