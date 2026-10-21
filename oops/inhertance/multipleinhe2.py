# Multiple Inheritance - Example 2
# Real-time Example: A SmartPhone inherits from both Phone and Camera

class Phone:
    def __init__(self):
        self.phone_brand = "Samsung"
        self.battery = "5000 mAh"

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, msg):
        print(f"Message sent: {msg}")

    def show_phone_info(self):
        print(f"Brand   : {self.phone_brand}")
        print(f"Battery : {self.battery}")


class Camera:
    def __init__(self):
        self.resolution = "108 MP"
        self.zoom = "10x Optical Zoom"

    def take_photo(self):
        print(f"Photo taken at {self.resolution}!")

    def record_video(self):
        print(f"Recording video with {self.zoom}...")

    def show_camera_info(self):
        print(f"Resolution : {self.resolution}")
        print(f"Zoom       : {self.zoom}")


# SmartPhone inherits from BOTH Phone and Camera
class SmartPhone(Phone, Camera):
    def __init__(self):
        Phone.__init__(self)
        Camera.__init__(self)
        self.model = "Galaxy S25 Ultra"
        self.os = "Android 16"

    def show_all_info(self):
        print(f"Model   : {self.model}")
        print(f"OS      : {self.os}")
        self.show_phone_info()
        self.show_camera_info()


# --- Using the SmartPhone ---
phone = SmartPhone()

print("===== SmartPhone Details =====")
phone.show_all_info()

print("\n===== Using Phone Features =====")
phone.make_call("9876543210")
phone.send_message("Hello, how are you?")

print("\n===== Using Camera Features =====")
phone.take_photo()
phone.record_video()

print("\n===== MRO =====")
# Shows the order Python searches for methods
for cls in SmartPhone.mro():
    print(f"  -> {cls.__name__}")
