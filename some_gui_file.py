import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#arbitrary stuff
class grid1(Gtk.Grid):
    def __init__(self,parent):
        Gtk.Grid.__init__(self,column_homogeneous=False, column_spacing=10,row_spacing=0)
        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        self.add(button1)

        self.text_file = Gtk.Entry()
        self.text_file.set_hexpand(True)
        self.attach(self.text_file, 1, 0, 4, 1)

        button2 = Gtk.Button("Choose Folder")
        button2.connect("clicked", self.on_folder_clicked)
        self.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 1)

        self.text_folder = Gtk.Entry()
        self.attach(self.text_folder, 1, 1, 4, 1)
    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self.get_toplevel(),
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.text_file.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self.get_toplevel(),
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            str1 = "Folder selected: " + dialog.get_filename()
            print(str1)
            self.fold_str = str1
            self.text_folder.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()



class content_grid2(Gtk.Grid):
    def __init__(self,maingrid):
        Gtk.Grid.__init__(self)
        imgbox = img_box(self)

        self.attach(imgbox,0,0,1,1)
        self.set_hexpand(True)

class img_box(Gtk.Box):
    def __init__(self,contentgrid2):
        Gtk.Box.__init__(self)
        someimg=Gtk.Image.new_from_icon_name("filenew",Gtk.IconSize.MENU)
        self.add(someimg)
        self.set_size_request(400,800)

class steps_box(Gtk.VBox):
    def __init__(self,maingrid):
        Gtk.VBox.__init__(self)
        btn1=Gtk.Button()
        btn1.set_image(Gtk.Image.new_from_icon_name("filenew",Gtk.IconSize.DIALOG))
        btn1.set_size_request(250,800)
        self.pack_start(btn1,False,False,0)


class maingrid(Gtk.Grid):
    def __init__(self,parent):
        Gtk.Grid.__init__(self)
        self.set_column_spacing(25)

        #arbitrary initialisations for underdeveloped stuff
        stepsbox = steps_box(self)
        contentgrid = content_grid2(self)



        #end of arbitary stuff
        self.attach(stepsbox,0,0,1,1)
        self.attach_next_to(contentgrid,stepsbox,Gtk.PositionType.RIGHT,1,1)


class mainwin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ghetto OMR")
        main = maingrid(self)
        self.add(main)
        self.maximize()


win = mainwin()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()







