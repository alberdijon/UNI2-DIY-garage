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
public class ProfitsPerMonth {
    private int totalPrice;
    private String date;
    public ProfitsPerMonth(int totalPrice,String date){
        this.date=date;
        this.totalPrice=totalPrice;
    }

    public int getTotalPrice() {
        return totalPrice;
    }

    public void setTotalPrice(int totalPrice) {
        this.totalPrice = totalPrice;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 83 * hash + this.totalPrice;
        hash = 83 * hash + Objects.hashCode(this.date);
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
        final ProfitsPerMonth other = (ProfitsPerMonth) obj;
        if (this.totalPrice != other.totalPrice) {
            return false;
        }
        if (!Objects.equals(this.date, other.date)) {
            return false;
        }
        return true;
    }
    
    
}
