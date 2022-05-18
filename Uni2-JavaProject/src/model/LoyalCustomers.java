/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.Objects;

/**
 *
<<<<<<< HEAD
 * @author agirrezabala.peru
=======
 * @author USUARIO
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
 */
public class LoyalCustomers {
    private String dni,name,surname;
    public LoyalCustomers(String dni,String name,String surname){
        this.dni=dni;
        this.name=name;
        this.surname=surname;
<<<<<<< HEAD
=======
      
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    @Override
    public int hashCode() {
<<<<<<< HEAD
        int hash = 5;
        hash = 79 * hash + Objects.hashCode(this.dni);
        hash = 79 * hash + Objects.hashCode(this.name);
        hash = 79 * hash + Objects.hashCode(this.surname);
=======
        int hash = 7;
        hash = 19 * hash + Objects.hashCode(this.dni);
        hash = 19 * hash + Objects.hashCode(this.name);
        hash = 19 * hash + Objects.hashCode(this.surname);
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final LoyalCustomers other = (LoyalCustomers) obj;
        if (!Objects.equals(this.dni, other.dni)) {
            return false;
        }
        if (!Objects.equals(this.name, other.name)) {
            return false;
        }
        if (!Objects.equals(this.surname, other.surname)) {
            return false;
        }
        return true;
    }
    
<<<<<<< HEAD
=======
    
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
}
