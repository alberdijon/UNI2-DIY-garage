/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.sql.Time;
import java.util.Objects;

/**
 *
 * @author rodriguez.markel
 */
public class NumberOfReservation {
      private int cabinId;
      private Time hour;
      private int numberOfReservations;

    public NumberOfReservation(int cabinId, Time hour, int numberOfReservations) {
        this.cabinId = cabinId;
        this.hour = hour;
        this.numberOfReservations = numberOfReservations;
    }

    public int getCabinId() {
        return cabinId;
    }

    public void setCabinId(int cabinId) {
        this.cabinId = cabinId;
    }

    public Time getHour() {
        return hour;
    }

    public void setHour(Time hour) {
        this.hour = hour;
    }

    public int getNumberOfReservations() {
        return numberOfReservations;
    }

    public void setNumberOfReservations(int numberOfReservations) {
        this.numberOfReservations = numberOfReservations;
    }

    @Override
    public String toString() {
        return "NumberOfReservation{" + "cabinId=" + cabinId + ", hour=" + hour + ", numberOfReservations=" + numberOfReservations + '}';
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
        final NumberOfReservation other = (NumberOfReservation) obj;
        if (this.cabinId != other.cabinId) {
            return false;
        }
        if (this.numberOfReservations != other.numberOfReservations) {
            return false;
        }
        if (!Objects.equals(this.hour, other.hour)) {
            return false;
        }
        return true;
    }
      
      
}
