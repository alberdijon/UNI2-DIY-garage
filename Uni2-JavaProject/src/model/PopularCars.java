/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.Objects;

/**
 *
 * @author agirrezabala.peru
 */
public class PopularCars {
    private String brand, model;
    private int cuantity;
    
    public PopularCars(String brand, String model, int cuantity){
        this.brand=brand;
        this.model=model;
        this.cuantity=cuantity;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getCuantity() {
        return cuantity;
    }

    public void setCuantity(int cuantity) {
        this.cuantity = cuantity;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 31 * hash + Objects.hashCode(this.brand);
        hash = 31 * hash + Objects.hashCode(this.model);
        hash = 31 * hash + this.cuantity;
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
        final PopularCars other = (PopularCars) obj;
        if (this.cuantity != other.cuantity) {
            return false;
        }
        if (!Objects.equals(this.brand, other.brand)) {
            return false;
        }
        if (!Objects.equals(this.model, other.model)) {
            return false;
        }
        return true;
    }

    

    
    
}
