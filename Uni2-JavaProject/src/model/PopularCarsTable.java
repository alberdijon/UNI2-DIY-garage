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
public class PopularCarsTable extends AbstractTableModel {
    private ArrayList<PopularCars> pcars = new ArrayList<>();
    private final String[] columnName = {"Brand", "Model"};
    
    public PopularCarsTable(ArrayList<PopularCars> regularCars){
        this.pcars=regularCars;
    }
    
    public int getRowCount(){
        return pcars.size();
    }
    
    public int getColumnCount(){
        return columnName.length;
    }
    public String getColumnName(int column){
        return columnName[column];
    }
    public Object getValueAt(int rowIndex, int columnIndex){
        switch(columnIndex){
            
            case 0: return pcars.get(rowIndex).getBrand();
            case 1: return pcars.get(rowIndex).getModel();


            default: return null;
        }
    
    }

}
   
