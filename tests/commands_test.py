import unittest
from unittest.mock import patch
from server import display_received_text


class TestServer(unittest.TestCase):

    def test_display_received_text_clear_display(self):
        expected_output = "Done: clear_display('white')\n"
        received_text = display_received_text("clear_display('white')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_pixel(self):
        expected_output = "Done: draw_pixel(10, 20, 'blue')\n"
        received_text = display_received_text("draw_pixel(10, 20, 'blue')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_line(self):
        expected_output = "Done: draw_line(30, 40, 50, 60, 'green')\n"
        received_text = display_received_text("draw_line(30, 40, 50, 60, 'green')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_rectangle(self):
        expected_output = "Done: draw_rectangle(70, 80, 100, 120, 'red')\n"
        received_text = display_received_text("draw_rectangle(70, 80, 100, 120, 'red')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_fill_rectangle(self):
        expected_output = "Done: fill_rectangle(90, 110, 150, 180, 'yellow')\n"
        received_text = display_received_text("fill_rectangle(90, 110, 150, 180, 'yellow')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_ellipse(self):
        expected_output = "Done: draw_ellipse(200, 220, 50, 70, 'orange')\n"
        received_text = display_received_text("draw_ellipse(200, 220, 50, 70, 'orange')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_fill_ellipse(self):
        expected_output = "Done: fill_ellipse(240, 260, 80, 100, 'purple')\n"
        received_text = display_received_text("fill_ellipse(240, 260, 80, 100, 'purple')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_circle(self):
        expected_output = "Done: draw_circle(300, 320, 30, 'pink')\n"
        received_text = display_received_text("draw_circle(300, 320, 30, 'pink')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_fill_circle(self):
        expected_output = "Done: fill_circle(340, 360, 40, 'brown')\n"
        received_text = display_received_text("fill_circle(340, 360, 40, 'brown')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_rounded_rectangle(self):
        expected_output = "Done: draw_rounded_rectangle(400, 420, 120, 140, 10, 'cyan')\n"
        received_text = display_received_text("draw_rounded_rectangle(400, 420, 120, 140, 10, 'cyan')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_fill_rounded_rectangle(self):
        expected_output = "Done: fill_rounded_rectangle(440, 460, 160, 180, 20, 'gray')\n"
        received_text = display_received_text("fill_rounded_rectangle(440, 460, 160, 180, 20, 'gray')")
        self.assertEqual(received_text, expected_output)

    def test_display_received_text_draw_text(self):
        expected_output = "Done: draw_text(500, 520, 'black', 12, 5, 'Hello')\n"
        received_text = display_received_text("draw_text(500, 520, 'black', 12, 5, 'Hello')")
        self.assertEqual(received_text, expected_output)


if __name__ == '__main__':
    unittest.main()
