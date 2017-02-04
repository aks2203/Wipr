###################################
#
# Avi Schwarzschild, Dan singer
# DevFest 2017
# Wipr App, gui
#
###################################

###--------------------------------------------------------------------------
import Tkinter as tk
from datetime import datetime, timedelta
import WiprModule as wp
import subprocess as sub

class WiprGUI():
    def __init__(self):
        '''init function to initialize an instance of the WiprGUI class'''

        # Ceate the main window.
        self.main_window = tk.Tk()
        self.main_window.configure(background='lightblue')
        self.main_window.title('WIPR')
        self.main_window.resizable(width=True, height=True)
        self.main_window.geometry('{}x{}'.format(1500, 800))

        # Create the frames to group widgets.
        self.title_frame = tk.Frame()
        self.top_frame = tk.Frame()
        self.mid_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.sub_frame = tk.Frame()

        self.title_frame.configure(background='lightblue')
        self.top_frame.configure(background='lightblue')
        self.mid_frame.configure(background='lightblue')
        self.bottom_frame.configure(background='lightblue')
        self.sub_frame.configure(background='lightblue')

        # Create title labels
        self.ready = tk.StringVar()
        self.ready.set('Do not filter untill files are ready!')
        self.title_label1 = tk.Label(self.title_frame, \
                                        text='WIPR', \
                                        bg='red', fg='white')
        self.title_label2 = tk.Label(self.title_frame, \
                                        text='weather for your ride', \
                                        bg='red', fg='white')
        self.title_space = tk.Label(self.title_frame, text='\n')

        # Pack 'em
        self.title_label1.pack(side='top')
        self.title_label2.pack(side='top')
        self.title_space.pack(side='bottom')

        # Input Output, file name entry spots:
        self.origin_label = tk.Label(self.top_frame, \
                    text='Enter starting point:', bg='blue', fg='white')
        self.origin_entry = tk.Entry(self.top_frame, width=20)
        self.dest_label = tk.Label(self.top_frame, \
                    text='Enter destination:', bg='blue', fg='white')
        self.dest_entry = tk.Entry(self.top_frame,  width=20)
        self.time_label = tk.Label(self.top_frame, \
                    text='Enter time to leave:', bg='blue', fg='white')
        self.time_entry = tk.Entry(self.top_frame,  width=20)
        self.top_space = tk.Label(self.top_frame, text='\n\n')

        # Pack top frame
        self.origin_label.pack(side='top')
        self.origin_entry.pack(side='top')
        self.dest_label.pack(side='top')
        self.dest_entry.pack(side='top')
        self.time_label.pack(side='top')
        self.time_entry.pack(side='top')
        self.top_space.pack(side='bottom')

        # # filter entry spots:
        # self.filter1_label = tk.Label(self.mid_frame, \
        #                                 text='Enter text to filter:')
        # self.textfilter_entry = tk.Entry(self.mid_frame, width=20)
        # self.filter2_label = tk.Label(self.mid_frame, \
        #                                 text='Enter state to filter:')
        # self.statefilter_entry = tk.Entry(self.mid_frame, width=20)
        # self.filter3_label = tk.Label(self.mid_frame, \
        #                                 text='Enter zip code to filter:')
        # self.zipfilter_entry = tk.Entry(self.mid_frame, width=20)
        # self.mid_space = tk.Label(self.mid_frame, \
        #                                 text='\n\n')

        # # Pack mid frame
        # self.filter1_label.pack(side='top')
        # self.textfilter_entry.pack(side='top')       
        # self.filter2_label.pack(side='top')
        # self.statefilter_entry.pack(side='top')         
        # self.filter3_label.pack(side='top')
        # self.zipfilter_entry.pack(side='top')
        # self.mid_space.pack(side='bottom')


        # Some buttons
        self.go_button = tk.Button(self.bottom_frame, \
                                     text='GO', \
                                     command=self.go, bg='black', \
                                     fg='white', activeforeground='blue')
        self.quit_button = tk.Button(self.bottom_frame, \
                                text='Quit', \
                                command=self.quit, bg='black', fg='white', \
                                activeforeground='blue')
        self.bottom_space = tk.Label(self.bottom_frame, text='\n\n')

        # Pack the buttons.
        self.go_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.bottom_space.pack(side='bottom')

        # Sub Frame
        self.weathermessage = tk.StringVar()
        self.weather_label = tk.Label(self.sub_frame, \
                                        textvariable=self.weathermessage, \
                                        fg='black', font=14)
        self.progressmessage = tk.StringVar()
        self.error_label = tk.Label(self.sub_frame, \
                                        textvariable=self.progressmessage, \
                                        fg='red', font=12)

        # Pack Sub frame
        self.weather_label.pack()
        self.error_label.pack()

        # Pack the frames
        self.title_frame.pack()
        self.top_frame.pack()
        # self.mid_frame.pack(side='right')
        self.bottom_frame.pack(side='bottom')
        self.sub_frame.pack(side='bottom')

        # Enter the Tkinter main loop.
        tk.mainloop() 

    def quit(self):
        '''quit function to close the window'''
        self.main_window.destroy()

    def go(self):
        '''go get everything from WiprModule'''
        # print self.origin_entry.get(), self.dest_entry.get()
        forcasts = wp.go(self.origin_entry.get(), self.dest_entry.get(), self.time_entry.get())
        # forcast_str = ['%s \n' % (i) for i in forcasts]
        # self.weathermessage.set(forcasts)
        times = [i[0] for i in forcasts]
        forcast_list = [i[1][0] for i in forcasts]
        icon_list = [i[1][1] for i in forcasts]


        file = open("output.txt")
        data = file.read()
        file.close()
        Results = tk.Label(self.main_window, text = data)
        Results.grid(row = 1, column = 1)

        # print forcasts
        # print type(times[0])

        # my_str = ''
        # for i in xrange(len(forcasts)):
        #     my_str += str(datetime.now() + timedelta(seconds=times[i])) # + str(forcast_list[i])+ '\n'
        # self.weathermessage.set(my_str)

        # p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
        # output, errors = p.communicate()

        # root = Tk()
        # text = Text(root)
        # text.pack()
        # text.insert(END, output)
        # root.mainloop()
        # self.progressmessage.set('Done!')

    def filter(self):
        '''runs the appropriate functions to put the data in the proper
        form, and then filters based on the user input conditions'''
        self.progressmessage.set('')
        if self.infile_entry.get() == '': self.error()
        if self.outfile_entry.get() == '': self.error()
        else:
            tweetlist = tweets.make_all_tweets(self.infile_entry.get())
            tweets.add_geo(tweetlist)
            tweets.write_tweets(tweetlist, self.outfile_entry.get())

            sentiment = tweets.make_sentiments('sentiments.csv')
            names = tweets.read_add_sentiments(self.outfile_entry.get(), \
                                                sentiment)

            province = self.statefilter_entry.get()
            zipcde = self.zipfilter_entry.get()
            wrd = self.textfilter_entry.get()

            if province != '':
                names = tweets.tweet_filter(names, state = province)
            if zipcde != '':
                names = tweets.tweet_filter(names, zip = zipcde)
            if wrd != '':
                names = tweets.tweet_filter(names, word = wrd)
            tweets.write_filtered_tweets(names, self.outfile_entry.get())
            self.progressmessage.set('Done!')

    def error(self):
        '''report if there's an error'''
        self.progressmessage.set('ERROR!')

# Create an instance 
tweet = WiprGUI()
# p = sub.Popen('./WiprModule.py',stdout=sub.PIPE,stderr=sub.PIPE)
# output, errors = p.communicate()

# root = Tk()
# text = Text(root)
# text.pack()
# text.insert(END, output)
# root.mainloop()

