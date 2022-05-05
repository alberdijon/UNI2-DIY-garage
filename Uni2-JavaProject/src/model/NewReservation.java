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
public class NewReservation {
    private int cabinId;
    private String clientDni;
    private Time hour;
    private Date date;
    private int total;

    public NewReservation(int cabinId, String clientDni, Time hour, Date date, int total) {
        this.cabinId = cabinId;
        this.clientDni = clientDni;
        this.hour = hour;
        this.date = date;
        this.total = total;
    }

    public int getCabinId() {
        return cabinId;
    }

    public void setCabinId(int cabinId) {
        this.cabinId = cabinId;
    }

    public String getClientDni() {
        return clientDni;
    }

    public void setClientDni(String clientDni) {
        this.clientDni = clientDni;
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

    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    @Override
    public String toString() {
        return "NewReservations{" + "cabinId=" + cabinId + ", clientDni=" + clientDni + ", hour=" + hour + ", date=" + date + ", total=" + total + '}';
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
        final NewReservation other = (NewReservation) obj;
        if (this.cabinId != other.cabinId) {
            return false;
        }
        if (this.total != other.total) {
            return false;
        }
        if (!Objects.equals(this.clientDni, other.clientDni)) {
            return false;
        }
        if (!Objects.equals(this.hour, other.hour)) {
            return false;
        }
        if (!Objects.equals(this.date, other.date)) {
            return false;
        }
        return true;
    }
    
    
}
