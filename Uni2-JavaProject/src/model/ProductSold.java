/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.sql.Date;
import java.sql.Time;

import java.util.Objects;

/**
 *
 * @author rodriguez.markel
 */
public class ProductSold {
    private String clientDni;
    private int productId;
    private int amount;
    private Date date;
    private Time hour;
    private int totalPrice;

    public ProductSold(String clientDni, int productId, int amount, Date date, Time hour, int totalPrice) {
        this.clientDni = clientDni;
        this.productId = productId;
        this.amount = amount;
        this.date = date;
        this.hour = hour;
        this.totalPrice = totalPrice;
    }

    public String getClientDni() {
        return clientDni;
    }

    public void setClientDni(String clientDni) {
        this.clientDni = clientDni;
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Time getHour() {
        return hour;
    }

    public void setHour(Time hour) {
        this.hour = hour;
    }

    public int getTotalPrice() {
        return totalPrice;
    }

    public void setTotalPrice(int totalPrice) {
        this.totalPrice = totalPrice;
    }

    @Override
    public String toString() {
        return "ProductSold{" + "clientDni=" + clientDni + ", productId=" + productId + ", amount=" + amount + ", date=" + date + ", hour=" + hour + ", totalPrice=" + totalPrice + '}';
    }

    @Override
    public int hashCode() {
        int hash = 7;
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
        if (this.productId != other.productId) {
            return false;
        }
        if (this.amount != other.amount) {
            return false;
        }
        if (this.totalPrice != other.totalPrice) {
            return false;
        }
        if (!Objects.equals(this.clientDni, other.clientDni)) {
            return false;
        }
        if (!Objects.equals(this.date, other.date)) {
            return false;
        }
        if (!Objects.equals(this.hour, other.hour)) {
            return false;
        }
        return true;
    }

    
    
}   