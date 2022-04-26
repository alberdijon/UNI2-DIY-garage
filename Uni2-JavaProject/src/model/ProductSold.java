/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.Objects;

/**
 *
 * @author rodriguez.markel
 */
public class ProductSold {
    public int id;
    public String brand;
    public String name;
    public int price;
    public int stock;

    public ProductSold(int id, String brand, String name, int price, int stock) {
        this.id = id;
        this.brand = brand;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    @Override
    public String toString() {
        return "Products{" + "id=" + id + ", brand=" + brand + ", name=" + name + ", price=" + price + ", stock=" + stock + '}';
    }

    @Override
    public int hashCode() {
        int hash = 5;
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
        final ProductSold other = (ProductSold) obj;
        if (this.id != other.id) {
            return false;
        }
        if (!Objects.equals(this.brand, other.brand)) {
            return false;
        }
        if (!Objects.equals(this.name, other.name)) {
            return false;
        }
        return true;
    }
    
    
}
