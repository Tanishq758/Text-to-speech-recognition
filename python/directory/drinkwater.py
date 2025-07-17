from win10toast import ToastNotifier

def send_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

if __name__ == '__main__':
   send_notification("Hello!", "Drink Water")