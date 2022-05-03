/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author rodriguez.markel
 */
public class NewReservationTable extends AbstractTableModel {
    private ArrayList<NewReservation> reservation = new ArrayList<>();
    private final String[] columnName = {"Cabin-ID, Client-DNI, Hour, Date, Total"};

     public NewReservationTable(ArrayList<NewReservation> reserve){
        this.reservation = reserve;
     
    }
     
    @Override
    public int getRowCount() {
        return reservation.size();
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
   
    @Override
    public String getColumnName(int column){
        return columnName[column];
    }
   
    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
       switch(columnIndex){
            case 0: return reservation.get(rowIndex).getClientDni();
            case 1: return reservation.get(rowIndex).getCabinId();
            case 2: return reservation.get(rowIndex).getDate();
            case 3: return reservation.get(rowIndex).getHour();
            case 4: return reservation.get(rowIndex).getTotal();
            default: return null;
        }
    }
   
}
