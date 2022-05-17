/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author agirrezabala.peru
 */
public class EmployeeOfTheMonthTable extends AbstractTableModel {
    private ArrayList<EmployeeOfTheMonth> memployee = new ArrayList<>();
    private final String[] columnName = {"ID", "Name", "Surname"};
    
    public EmployeeOfTheMonthTable(ArrayList<EmployeeOfTheMonth> bestworker){
        this.memployee=bestworker;
     
    }
    @Override
    public int getRowCount() {
        return memployee.size();
    }
    public int getColumnCount(){
        return columnName.length;
    }
    @Override
    public String getColumnName(int column){
        return columnName[column];
    }
    public Object getValueAt(int rowIndex, int columnIndex) {
        
        switch(columnIndex){
            
            case 0: return memployee.get(rowIndex).getId();
            case 1: return memployee.get(rowIndex).getName();
            case 2: return memployee.get(rowIndex).getSurname();


            default: return null;
        }
    }
    
}
