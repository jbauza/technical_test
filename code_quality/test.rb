# This class is used for logins
class Login
  attr_reader :sessions, :users, :passwords

  # Receives a hash with usernames as keys and passwords as values
  def initialize(hash)
    @sessions = []
    @users = []
    @passwords = []
    hash.map do |k,v|
      @users = @users + [k]
      @passwords = @passwords + [v]
    end
  end

  def logout(user)
    sessions.each_with_index do |session, i|
      sessions[i] = nil if session == user
    end
    sessions.compact!
  end

  # Checks if user exists
  def user_exists(user)
    # Temp variable for storing the user if found
    temp = ''
    for i in users
      if i == user
        temp = user
      end
    end
    exists = temp != '' && temp == user
    exists
  end

  # Register user
  def register_user(user, password)
    last_index = users.size
    users[last_index] = user
    passwords[last_index] = password
  end

  def remove_user(user)
    index = idx(user, users)
    users[index] = nil
    passwords[index] = nil
    users.compact!
    passwords.compact!
  end

  def check_password(user, password)
    index = idx(user, users)
    password_correct = passwords[index] == password
    return password_correct
  end

  def update_password(user, old_password, new_password)
    # First we check if the user exists
    user_1 = ''
    for i in users
      if i == user
        user_1 = user
      end
    end
    if user_1 == user
      index = idx(user, users)
      if passwords[index] == old_password
        passwords[index] = new_password
        return true
      end
    end
    return false
  end

  def login(user, password)
    index = idx(user, users)
    if passwords[index] == password
      sessions << user
    end
  end

  # Gets index of an element in an array
  def idx(element, array)
    cont=0
    for i in array
      return cont if i == element
      cont += 1
    end
    return cont
  end
end



registered_users = {
  'user1' => 'pass1',
  'user2' => 'pass2',
  'user3' => 'pass3'
}

login = Login.new(registered_users)
puts("Registered Users: #{login.users}")
puts("Registered Passwords: #{login.passwords}")
puts("User -user1- exists? #{login.user_exists('user1')}")
puts("User -user7- exists? #{login.user_exists('user7')}")
puts("Register -user9- pass: -pass9- #{login.register_user('user9', 'pass9')}")
puts("LOGIN: #{login.inspect}")
puts("User -user9- exists? #{login.user_exists('user9')}")
puts("Change Password -user9- to -pass1000- #{login.update_password('user9', 'pass9', 'pass1000')}")
puts("LOGIN: #{login.inspect}")
puts("Login -user9- #{login.login('user9', 'pass1000')}")
puts("LOGIN: #{login.inspect}")
puts("Logout -user9- #{login.logout('user9')}")
puts("LOGIN: #{login.inspect}")
puts("Check password -user9- correct #{login.check_password('user9', 'pass1000')}")
puts("Check password -user9- incorrect #{login.check_password('user9', 'pass9')}")
puts("Remove User -user9- #{login.remove_user('user9')}")
puts("LOGIN: #{login.inspect}")
