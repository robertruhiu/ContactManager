class Marker:
    def __init__(self, color = "Red"):
        self.color = color


class MarkerBox:
    # noinspection PyShadowingNames
    def __init__(self, markers = None):  # markers list is initiated here
        if markers is None:
            markers = []
        self.markers = markers

    def add_marker(self, marker):

        self.markers.append(marker)

    def remove_marker(self, color):
        for marker in self.markers:
            if marker.color == color:
                self.markers.remove(marker)
                return marker
            return None


if __name__ == "__main__":

    mest_markers = MarkerBox()
    mest_markers.add_marker(Marker(color = "blue"))
    mest_markers.add_marker(Marker(color = "black"))
    mest_markers.add_marker(Marker())  # fetches the default variable of red
    mest_markers.remove_marker("blue")

    for markers in mest_markers.markers:  # the .markers is the list we are accessing
        print(markers.color)

    print("The marker box has {} markers".format(len(mest_markers.markers)))
