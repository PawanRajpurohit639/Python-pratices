from threading import *
from time import sleep

class TExample(Thread):

    def __init__(self,Text):
        super(TExample,self).__init__()
        self.Text = Text
        #super.__init__()
    def run(self):
        with open("test.txt","a+") as file:
            file.write(self.Text+"\n")
            
        #print("Text")
        return super().run()

"""for i in range(1,15):
    testData = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tincidunt nunc sed odio dapibus fringilla. Proin ullamcorper eros non orci ultricies rutrum eget nec sem. Curabitur eros elit, gravida id diam et, consequat imperdiet leo. Nunc tincidunt dictum purus, quis dictum metus pellentesque id. Suspendisse sed blandit sapien. Aliquam at ultricies justo. Aenean tempor diam eget urna maximus tristique. Etiam pretium sed augue vel pretium. Maecenas purus tortor, fermentum at dignissim ac, tincidunt vitae orci. Curabitur pharetra suscipit dolor, quis scelerisque ligula ullamcorper id. Etiam ac orci maximus felis mollis sagittis nec non lectus. Nunc ac lorem ligula. Aliquam ullamcorper pharetra tincidunt. Morbi convallis semper turpis in eleifend. Maecenas porttitor mauris in tellus interdum laoreet. Nunc tempor hendrerit tortor, at porta lorem congue nec. Donec vestibulum sit amet lacus sed varius. Duis sit amet placerat sapien. Suspendisse vestibulum faucibus neque iaculis facilisis. Curabitur aliquam magna sit amet quam rhoncus ultricies. Vivamus vulputate pretium augue sit amet elementum. Sed sollicitudin vel massa vel volutpat. Quisque eget risus nisi. Sed sodales ac velit vitae auctor. Proin aliquam efficitur velit, in maximus sem facilisis a. Pellentesque tempor velit non quam condimentum sagittis. Proin tempus leo eu nibh facilisis, laoreet cursus nunc hendrerit. Donec pulvinar libero mollis velit ornare, eu sodales massa euismod. Aliquam metus elit, consequat id libero a, tristique aliquam velit. Praesent dui nisi, egestas vel felis sed, euismod dignissim mauris. Donec id justo maximus, gravida ipsum eget, vulputate ligula. Nullam sem arcu, molestie ac scelerisque et, rutrum nec lacus. Proin tempor arcu eu metus iaculis, id tristique lectus sagittis. Curabitur sollicitudin felis vitae diam vestibulum porta. Integer consectetur, arcu non pellentesque cursus, est ligula aliquet purus, eget blandit ligula quam vel eros. Suspendisse vitae libero eros. Vivamus elit dolor, viverra eget interdum id, molestie non nunc. Nullam viverra mattis tristique. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In facilisis bibendum sapien sed finibus. Donec hendrerit tempus tincidunt. Ut interdum urna tellus, vel efficitur dolor viverra ac. Nullam iaculis commodo libero ut tempus. Phasellus lobortis, sem a sodales feugiat, nulla eros cursus metus, ut scelerisque neque nunc id lectus. Fusce auctor augue vel est finibus tincidunt. Aliquam nec pretium dolor, facilisis vehicula odio. Vivamus in arcu faucibus, gravida nulla at, consequat diam. Aliquam erat volutpat. Duis ac leo in leo viverra consequat. Ut cursus sem quam, nec consectetur est tempus vitae. Pellentesque consectetur libero nec arcu facilisis faucibus.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tincidunt nunc sed odio dapibus fringilla. Proin ullamcorper eros non orci ultricies rutrum eget nec sem. Curabitur eros elit, gravida id diam et, consequat imperdiet leo. Nunc tincidunt dictum purus, quis dictum metus pellentesque id. Suspendisse sed blandit sapien. Aliquam at ultricies justo. Aenean tempor diam eget urna maximus tristique. Etiam pretium sed augue vel pretium. Maecenas purus tortor, fermentum at dignissim ac, tincidunt vitae orci. Curabitur pharetra suscipit dolor, quis scelerisque ligula ullamcorper id. Etiam ac orci maximus felis mollis sagittis nec non lectus. Nunc ac lorem ligula. Aliquam ullamcorper pharetra tincidunt. Morbi convallis semper turpis in eleifend. Maecenas porttitor mauris in tellus interdum laoreet. Nunc tempor hendrerit tortor, at porta lorem congue nec. Donec vestibulum sit amet lacus sed varius. Duis sit amet placerat sapien. Suspendisse vestibulum faucibus neque iaculis facilisis. Curabitur aliquam magna sit amet quam rhoncus ultricies. Vivamus vulputate pretium augue sit amet elementum. Sed sollicitudin vel massa vel volutpat. Quisque eget risus nisi. Sed sodales ac velit vitae auctor. Proin aliquam efficitur velit, in maximus sem facilisis a. Pellentesque tempor velit non quam condimentum sagittis. Proin tempus leo eu nibh facilisis, laoreet cursus nunc hendrerit. Donec pulvinar libero mollis velit ornare, eu sodales massa euismod. Aliquam metus elit, consequat id libero a, tristique aliquam velit. Praesent dui nisi, egestas vel felis sed, euismod dignissim mauris. Donec id justo maximus, gravida ipsum eget, vulputate ligula. Nullam sem arcu, molestie ac scelerisque et, rutrum nec lacus. Proin tempor arcu eu metus iaculis, id tristique lectus sagittis. Curabitur sollicitudin felis vitae diam vestibulum porta. Integer consectetur, arcu non pellentesque cursus, est ligula aliquet purus, eget blandit ligula quam vel eros. Suspendisse vitae libero eros. Vivamus elit dolor, viverra eget interdum id, molestie non nunc. Nullam viverra mattis tristique. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In facilisis bibendum sapien sed finibus. Donec hendrerit tempus tincidunt. Ut interdum urna tellus, vel efficitur dolor viverra ac. Nullam iaculis commodo libero ut tempus. Phasellus lobortis, sem a sodales feugiat, nulla eros cursus metus, ut scelerisque neque nunc id lectus. Fusce auctor augue vel est finibus tincidunt. Aliquam nec pretium dolor, facilisis vehicula odio. Vivamus in arcu faucibus, gravida nulla at, consequat diam. Aliquam erat volutpat. Duis ac leo in leo viverra consequat. Ut cursus sem quam, nec consectetur est tempus vitae. Pellentesque consectetur libero nec arcu facilisis faucibus."
    obj1 = Thread(target=TExample(testData+" "+str(i)+"\n").run(), args=())
    obj1.start()
    obj2 = Thread(target=TExample(testData+" "+str(i)+"\n").run(), args=())
    obj2.start()
    obj3 = Thread(target=TExample(testData+" "+str(i)+"\n").run(), args=())
    obj3.start()
    obj4 = Thread(target=TExample(testData+" "+str(i)+"\n").run(), args=())
    obj4.start()
    obj5 = Thread(target=TExample(testData+" "+str(i)+"\n").run(), args=())
    obj5.start()
    obj1.join()
    obj2.join()
    obj3.join()
    obj4.join()
    obj5.join()"""

testData = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tincidunt nunc sed odio dapibus fringilla. Proin ullamcorper eros non orci ultricies rutrum eget nec sem. Curabitur eros elit, gravida id diam et, consequat imperdiet leo. Nunc tincidunt dictum purus, quis dictum metus pellentesque id. Suspendisse sed blandit sapien. Aliquam at ultricies justo. Aenean tempor diam eget urna maximus tristique. Etiam pretium sed augue vel pretium. Maecenas purus tortor, fermentum at dignissim ac, tincidunt vitae orci. Curabitur pharetra suscipit dolor, quis scelerisque ligula ullamcorper id. Etiam ac orci maximus felis mollis sagittis nec non lectus. Nunc ac lorem ligula. Aliquam ullamcorper pharetra tincidunt. Morbi convallis semper turpis in eleifend. Maecenas porttitor mauris in tellus interdum laoreet. Nunc tempor hendrerit tortor, at porta lorem congue nec. Donec vestibulum sit amet lacus sed varius. Duis sit amet placerat sapien. Suspendisse vestibulum faucibus neque iaculis facilisis. Curabitur aliquam magna sit amet quam rhoncus ultricies. Vivamus vulputate pretium augue sit amet elementum. Sed sollicitudin vel massa vel volutpat. Quisque eget risus nisi. Sed sodales ac velit vitae auctor. Proin aliquam efficitur velit, in maximus sem facilisis a. Pellentesque tempor velit non quam condimentum sagittis. Proin tempus leo eu nibh facilisis, laoreet cursus nunc hendrerit. Donec pulvinar libero mollis velit ornare, eu sodales massa euismod. Aliquam metus elit, consequat id libero a, tristique aliquam velit. Praesent dui nisi, egestas vel felis sed, euismod dignissim mauris. Donec id justo maximus, gravida ipsum eget, vulputate ligula. Nullam sem arcu, molestie ac scelerisque et, rutrum nec lacus. Proin tempor arcu eu metus iaculis, id tristique lectus sagittis. Curabitur sollicitudin felis vitae diam vestibulum porta. Integer consectetur, arcu non pellentesque cursus, est ligula aliquet purus, eget blandit ligula quam vel eros. Suspendisse vitae libero eros. Vivamus elit dolor, viverra eget interdum id, molestie non nunc. Nullam viverra mattis tristique. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In facilisis bibendum sapien sed finibus. Donec hendrerit tempus tincidunt. Ut interdum urna tellus, vel efficitur dolor viverra ac. Nullam iaculis commodo libero ut tempus. Phasellus lobortis, sem a sodales feugiat, nulla eros cursus metus, ut scelerisque neque nunc id lectus. Fusce auctor augue vel est finibus tincidunt. Aliquam nec pretium dolor, facilisis vehicula odio. Vivamus in arcu faucibus, gravida nulla at, consequat diam. Aliquam erat volutpat. Duis ac leo in leo viverra consequat. Ut cursus sem quam, nec consectetur est tempus vitae. Pellentesque consectetur libero nec arcu facilisis faucibus.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tincidunt nunc sed odio dapibus fringilla. Proin ullamcorper eros non orci ultricies rutrum eget nec sem. Curabitur eros elit, gravida id diam et, consequat imperdiet leo. Nunc tincidunt dictum purus, quis dictum metus pellentesque id. Suspendisse sed blandit sapien. Aliquam at ultricies justo. Aenean tempor diam eget urna maximus tristique. Etiam pretium sed augue vel pretium. Maecenas purus tortor, fermentum at dignissim ac, tincidunt vitae orci. Curabitur pharetra suscipit dolor, quis scelerisque ligula ullamcorper id. Etiam ac orci maximus felis mollis sagittis nec non lectus. Nunc ac lorem ligula. Aliquam ullamcorper pharetra tincidunt. Morbi convallis semper turpis in eleifend. Maecenas porttitor mauris in tellus interdum laoreet. Nunc tempor hendrerit tortor, at porta lorem congue nec. Donec vestibulum sit amet lacus sed varius. Duis sit amet placerat sapien. Suspendisse vestibulum faucibus neque iaculis facilisis. Curabitur aliquam magna sit amet quam rhoncus ultricies. Vivamus vulputate pretium augue sit amet elementum. Sed sollicitudin vel massa vel volutpat. Quisque eget risus nisi. Sed sodales ac velit vitae auctor. Proin aliquam efficitur velit, in maximus sem facilisis a. Pellentesque tempor velit non quam condimentum sagittis. Proin tempus leo eu nibh facilisis, laoreet cursus nunc hendrerit. Donec pulvinar libero mollis velit ornare, eu sodales massa euismod. Aliquam metus elit, consequat id libero a, tristique aliquam velit. Praesent dui nisi, egestas vel felis sed, euismod dignissim mauris. Donec id justo maximus, gravida ipsum eget, vulputate ligula. Nullam sem arcu, molestie ac scelerisque et, rutrum nec lacus. Proin tempor arcu eu metus iaculis, id tristique lectus sagittis. Curabitur sollicitudin felis vitae diam vestibulum porta. Integer consectetur, arcu non pellentesque cursus, est ligula aliquet purus, eget blandit ligula quam vel eros. Suspendisse vitae libero eros. Vivamus elit dolor, viverra eget interdum id, molestie non nunc. Nullam viverra mattis tristique. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In facilisis bibendum sapien sed finibus. Donec hendrerit tempus tincidunt. Ut interdum urna tellus, vel efficitur dolor viverra ac. Nullam iaculis commodo libero ut tempus. Phasellus lobortis, sem a sodales feugiat, nulla eros cursus metus, ut scelerisque neque nunc id lectus. Fusce auctor augue vel est finibus tincidunt. Aliquam nec pretium dolor, facilisis vehicula odio. Vivamus in arcu faucibus, gravida nulla at, consequat diam. Aliquam erat volutpat. Duis ac leo in leo viverra consequat. Ut cursus sem quam, nec consectetur est tempus vitae. Pellentesque consectetur libero nec arcu facilisis faucibus."
obj1 = Thread(target=TExample(testData+" 1\n").run(), args=())
obj2 = Thread(target=TExample(testData+" 2\n").run(), args=())
obj3 = Thread(target=TExample(testData+" 3\n").run(), args=())
obj4 = Thread(target=TExample(testData+" 4\n").run(), args=())
obj5 = Thread(target=TExample(testData+" 5\n").run(), args=())
obj1.start()
obj2.start()
obj3.start()
obj4.start()
obj5.start()
obj1.join()
obj2.join()
obj3.join()
obj4.join()
obj5.join()


"""obj2 = TExample("test2")
obj3 = TExample()
obj4 = TExample()
obj5 = TExample()
obj6 = TExample()
obj7 = TExample()
obj8 = TExample()
obj9 = TExample()
obj10 = TExample()
obj11 = TExample()
obj12 = TExample()
obj13 = TExample()
obj14 = TExample()
obj15 = TExample()"""



"""obj1.demo("test")
obj2.demo("test1")
obj3.demo("test3")
obj4.demo("test4")
obj5.demo("test5")
obj6.demo("test6")
obj7.demo("test7")
obj8.demo("test8")
obj9.demo("test9")
obj10.demo("test10")
obj11.demo("test11")
obj12.demo("test12")
obj13.demo("test13")
obj14.demo("test14")
obj15.demo("test15")"""