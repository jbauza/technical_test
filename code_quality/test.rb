# This class is used for logins
class Login
=begin 
Cambios aplicados:
1. Convertir arreglos de users y passwords a un hash que es mucho mas eficiente para acceder a los datos.
2. Se cambia la capacidad de leer las variables users y passwords directamente y se agregan metodos que los devuelven como la antigua representacion para no variar los resultados.
=end
  attr_reader :sessions

  # Receives a hash with usernames as keys and passwords as values
  def initialize(hash)
    @sessions = []
    @users = hash
  end
  #metodo para retornar misma representacion anterior de users
  def users
    @users.each_key.to_a
  end
  #metodo para retornar misma representacion anterior de passwords
  def passwords
    @users.each_value.to_a
  end

  def logout(user)
    sessions.each_with_index do |session, i|
      sessions[i] = nil if session == user
    end
    sessions.compact!
  end

  # Checks if user exists
  def user_exists(user)
    @users.key?(user)
  end

  # Register user
  def register_user(user, password)
    @users[user] = password
  end

  def remove_user(user)
    @users.delete(user)
    passwords
  end

  def check_password(user, password)
    @users[user] == password
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
      if @users[user] == old_password
        @users[user] = new_password
        return true
      end
    end
    return false
  end

  def login(user, password)
    if @users[user] == password
      sessions << user
    end
  end

  # Gets index of an element in an array
  # Se comenta pues ya no es necesaria, en proximos comits se quita
=begin
  def idx(element, array)
    cont=0
    for i in array
      return cont if i == element
      cont += 1
    end
    return cont
  end
=end
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
