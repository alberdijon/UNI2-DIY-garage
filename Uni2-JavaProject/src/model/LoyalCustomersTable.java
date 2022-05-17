/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author USUARIO
 */
public class LoyalCustomersTable extends AbstractTableModel {
    private ArrayList<LoyalCustomers> lcustomer =new ArrayList<>();
    private final String[] columnName = {"DNI", "Name", "Surname"};
    
    public LoyalCustomersTable(ArrayList<LoyalCustomers> bestcustomer){
        this.lcustomer=bestcustomer;
    }

    @Override
    public int getRowCount() {
       return lcustomer.size();

    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        switch(columnIndex){
            
            case 0: return lcustomer.get(rowIndex).getDni();
            case 1: return lcustomer.get(rowIndex).getName();
            case 2: return lcustomer.get(rowIndex).getSurname();


            default: return null;
        }
    }
    
}
