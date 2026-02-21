

test_settings = {'Theme': 'light'}
def add_setting(settings,new_setting):
    key = new_setting[0].lower()
    value= new_setting[1].lower()

    
    # Cek apakah key sudah ada di dictionary
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Tambahkan jika belum ada
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"



def update_setting(settings,new_update):
    key = new_update[0].lower()
    value = new_update[1].lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings , key):
    key=key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return f"Setting not found!"




def view_settings(settings):
    if len(settings) == 0:
        return "No settings available."
    
    else:
        output=""
        for key,value in settings.items():        
            output+= f"{key.capitalize()}: {value}\n"
        return f"Current User Settings:\n{output}"



add_setting(test_settings,("Usia", "Muda"))
add_setting(test_settings,('Blue','Red'))
print(view_settings(test_settings))




