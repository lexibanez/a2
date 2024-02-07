from Profile import Profile, Post

def test_profile():
    lex = Profile('server', 'lexibanez', '10202004')
    lex.save_profile(r'C:\Users\lexib\OneDrive\Desktop\ICS32\assignments\a2\testpath.dsu')

if __name__ == '__main__':
    test_profile()
    